import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


import plotly.graph_objects as go
import math


data = pd.read_csv("./dataset/demand.csv")
# data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/demand.csv")
data.head()


print(data.head())
data = data.dropna() # Remove the values that contains null values


##  Scatter plot  ##
def displayScatterPlot():
    # We can see that most of the data points show the sales of the product is
    # increasing as the price is decreasing with some exceptions:
    fig = px.scatter(data, x="Units Sold", y="Total Price",
                    size='Units Sold')
    fig.show()



## Correlational Heatmap plot  ##
def displayCorrelationalHeatmap():
    correlations = data.corr(method='pearson')
    plt.figure(figsize=(15, 12))
    sns.heatmap(correlations, cmap="coolwarm", annot=True)
    plt.show()


# Visualize the 2 plots to gain a deeper insight before developing the prediction model
def displayVisualAnalysis():
    displayScatterPlot()
    displayCorrelationalHeatmap()



###   Product Demand Prediction Model   ###
def buildPredictiveModel():
    # Now let’s move to the task of training a machine learning model to predict the demand
    # for the product at different prices. I will choose the Total Price and the Base Price
    # column as the features to train the model, and the Units Sold column as labels for the model:

    x = data[["Total Price", "Base Price"]]
    y = data["Units Sold"]



    # Now let’s split the data into training and test sets and use the decision tree regression algorithm
    # to train our model:

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.2, 
                                                    random_state=42)
    from sklearn.tree import DecisionTreeRegressor
    model = DecisionTreeRegressor()
    model.fit(xtrain, ytrain)

    return model



# Now let’s input the features (Total Price, Base Price) into the model and predict how much quantity can be
# demanded based on those values:
def runNumericalTestCases(model):
    #features = [["Total Price", "Base Price"]]
    features = np.array([[133.00, 140.00]])
    print(model.predict(features))



    features = np.array([[99.0375, 111.8625]]) # OUTPUT: [70.75]
    print(model.predict(features))


    features = np.array([[99.0375, 105.8625]]) # OUTPUT: [88.]
    print(model.predict(features))


    # If the stores puts too low of a price, we humans have a propensity to think that the product isn't socially valued,
    # and therefore not worth purchasing. Conversely, when increasing the price the product automatically appears as a
    # premium product of stature and in turn becomes more appealing. For instance, if a Lamborghini's price would be
    # diminished to only $50.000, it would become more common in society at the expense of its uniqueness. In the end,
    # people would cease buying it because it's nothing special about it anymore: it's flashy status that the product
    # carried eradicated in parallel with the decline of its price.
    features = np.array([[99.0375, 100.8625]]) # OUTPUT: [9.]
    print(model.predict(features))


    features = np.array([[99.0375, 104.8625]]) # OUTPUT: [128.]
    print(model.predict(features))


    features = np.array([[99.0375, 103.8625]]) # OUTPUT: [107.]
    print(model.predict(features))



def displayLineChart(model):
    # Y-values = Predicted Quantity
    yValueArray = []
    xValueArray = []

    numInstances = 5
    increment = 5

    basePrice = 99.0375
    bsStart = math.ceil(basePrice) # basePrice start value in the for-loop iteration


    # basePrice + (increment * n)
    endValue = bsStart + (increment * numInstances)

    # i = currentTotalPrice
    for i in range(bsStart, endValue, increment):

        featuresCase = np.array([[basePrice, i]])
        profitMargin = model.predict(featuresCase)

        xValueArray.append(i)
        yValueArray.append(profitMargin[0])

        # Print the current data-instance to be displayed on the line chart
        # print(f"CURRENT: y = {profitMargin[0]}, x = {i}")


    # Print all the data-instances to be displayed on the line chart
    # print(xValueArray)
    # print(yValueArray)


    f1 = go.Figure(
        data = [
            go.Scatter(x=xValueArray, y=yValueArray, name="first"),
        ],
        layout = {"xaxis": {"title": "Total Price (Product's selling price in the store)"}, "yaxis": {"title": "Predicted Purchase Quantity"}, "title": f"Predicted customer purchase quantity of a product with Base Price {basePrice}"}
    )
    f1.show()


def runMain():
    model = buildPredictiveModel()
    runNumericalTestCases(model)

    displayLineChart(model)
    displayVisualAnalysis()


runMain()