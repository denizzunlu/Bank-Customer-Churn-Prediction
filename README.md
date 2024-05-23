# Kaggle Playground Series S4E1 - Customer Churn Prediction

This Notebook was prepared for [Kaggle Playground Series S4E1](https://www.kaggle.com/competitions/playground-series-s4e1/overview) and achieved a score of 0.89844. It has been deployed using Flask API on HEROKU.

Link: https://bankcustomerchurnpred-5c48d8489ff5.herokuapp.com/

![0_n7vG65S6qTv7KhZK](https://github.com/denizzunlu/Bank-Customer-Churn-Prediction/assets/123365405/ccc31f05-84e9-44fd-9b09-8105dd553534)



## About

**Goal:** To predict whether a customer will continue to use their account or close it.

**Evaluation:** Submissions are evaluated on area under the ROC curve between the predicted probability and the observed target.

The bank customer churn dataset is a commonly used dataset for predicting customer churn in the banking industry. It contains information on bank customers who either left the bank or continue to be a customer. The dataset includes the following attributes:

- **Customer ID:** A unique identifier for each customer
- **Surname:** The customer's surname or last name
- **Credit Score:** A numerical value representing the customer's credit score
- **Geography:** The country where the customer resides (France, Spain, or Germany)
- **Gender:** The customer's gender (Male or Female)
- **Age:** The customer's age.
- **Tenure:** The number of years the customer has been with the bank
- **Balance:** The customer's account balance
- **NumOfProducts:** The number of bank products the customer uses (e.g., savings account, credit card)
- **HasCrCard:** Whether the customer has a credit card (1 = yes, 0 = no)
- **IsActiveMember:** Whether the customer is an active member (1 = yes, 0 = no)
- **EstimatedSalary:** The estimated salary of the customer
- **Exited:** Whether the customer has churned (1 = yes, 0 = no)
