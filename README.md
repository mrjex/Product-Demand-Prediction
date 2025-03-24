# Product Demand Prediction 📊

> An intelligent machine learning system for optimizing product pricing strategies

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Regression-green)](https://scikit-learn.org/)
[![Data Science](https://img.shields.io/badge/Data-Analysis-orange)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success)](https://github.com/yourusername/Product-Demand-Prediction)

## 📑 Table of Contents

- [Product Demand Prediction 📊](#product-demand-prediction-)
  - [📑 Table of Contents](#-table-of-contents)
  - [🎯 Overview](#-overview)
    - [🎬 Demonstration](#-demonstration)
  - [💼 Business Challenge](#-business-challenge)
  - [✨ Key Features](#-key-features)
  - [🧮 Prediction Model](#-prediction-model)
    - [Key Relationships](#key-relationships)
  - [🚀 Development Journey](#-development-journey)
    - [1. Numerical Discovery](#1-numerical-discovery)
    - [2. Hypothesis Formation](#2-hypothesis-formation)
    - [3. Conceptual Framework](#3-conceptual-framework)
    - [4. Implementation](#4-implementation)
  - [📈 Results \& Insights](#-results--insights)
  - [🚀 Getting Started](#-getting-started)

## 🎯 Overview

This project utilizes machine learning to predict product demand based on pricing variables, helping retailers optimize their pricing strategy for maximum revenue. Developed in June 2024, it addresses the perennial challenge of inventory management by establishing the optimal price point that balances demand, perceived value, and profit margins.

### 🎬 Demonstration

![demo](demo.mp4)
*Interactive prediction system showing real-time demand forecasting*

## 💼 Business Challenge

Retailers face a critical dilemma: **How do you price products to maximize both sales volume and profit?**

This project tackles several key business questions:
- 📉 How does price reduction affect customer perception and product status?
- 💰 What is the relationship between price reduction and profit margin erosion?
- 📈 Where is the optimal price point that maximizes total revenue?

> "The art of pricing involves finding the sweet spot where perceived value meets profit optimization."

## ✨ Key Features

- **Demand Forecasting**: Predict sales volume based on pricing inputs
- **Price Optimization**: Identify the optimal price point for maximum revenue
- **Status-Value Analysis**: Account for the psychological aspects of pricing
- **Profit Margin Calculation**: Visualize the relationship between price and profitability

## 🧮 Prediction Model

The system uses two primary variables to generate demand predictions:

| Variable | Description | Business Significance |
|----------|-------------|----------------------|
| **Base Price** | The retail price charged to customers | Determines consumer appeal and perceived value |
| **Total Price** | The cost paid to suppliers for the product | Establishes the underlying market value and scarcity |

### Key Relationships

- **Profit Margin** = Base Price - Total Price
- **Business Constraint**: Total Price < Base Price (fundamental profit requirement)

The model uncovers the non-linear relationship between price reduction and demand increase, accounting for the psychological threshold where:
- 📊 Too low a price diminishes perceived value and status
- 📊 Strategically higher prices can create premium positioning

## 🚀 Development Journey

This project evolved through a methodical process of observation, analysis, and implementation:

### 1. Numerical Discovery
![Numerical Observation](development-process/1.%20Numerical%20Observation.PNG)

*Initial data exploration revealing price-demand patterns*

Initial model testing revealed a fascinating pattern: decreasing prices increased predicted demand, but this relationship wasn't linear and raised critical questions about optimal pricing strategy.

### 2. Hypothesis Formation
![Idea Formation](development-process/2.%20Idea%20was%20born%20and%20articulated.PNG)

*Documentation of hypotheses and analytical approach*

The McDonald's paradox emerged: low prices generate volume but sacrifice status and margins. Luxury restaurants leverage higher prices for fewer sales but larger profits. This led to the central question: **What matters more—volume or margin?**

### 3. Conceptual Framework
![Conceptual Design](development-process/3.%20Conceptualized%20Idea.jpg)

*Visual mapping of the optimization algorithm*

A methodical framework was developed to find the optimal price point where revenue (Price × Volume) is maximized, accounting for both margin and perceived value constraints.

### 4. Implementation
![Implementation](development-process/4.%20Implemented%20Idea.PNG)

*Final system with automated price optimization*

The fully implemented system now automatically calculates and visualizes the revenue-optimizing price point, providing actionable business intelligence.

## 📈 Results & Insights

The model revealed several counter-intuitive insights:

1. **Price Elasticity Threshold**: There exists a point below which further price reductions actually harm total revenue
2. **Status-Value Curve**: Products demonstrate a psychological pricing curve where perceived value peaks at an optimal price point
3. **Revenue Maximization**: The optimal price point for revenue maximization is rarely the lowest possible price

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the prediction model:
   ```bash
   python demand_prediction.py
   ```
4. Input your product's base price and cost to receive:
   - Predicted demand
   - Revenue forecast
   - Optimal price recommendation

---

*Developed by Joel Mattsson using Python and machine learning techniques*