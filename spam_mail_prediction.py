# -*- coding: utf-8 -*-
"""SPAM_MAIL_PREDICTION.ipynb
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""data collection and preprocessing"""

# loading the data from csv file to a pandas Dataframe
raw_mail_data=pd.read_csv('/mail_data.csv')

print(raw_mail_data)

# replace the null values with a null string 
mail_data=raw_mail_data.where((pd.notnull(raw_mail_data)),'')

# printing the forst five rows of the data frame 
mail_data.head()

# checking the number of rows and columns in the dataframe
mail_data.shape

"""Label Encoding"""

# label spam mail as 0 , ham mail as 1;
mail_data.loc[mail_data['Category'] =='spam', 'Category',] =0
mail_data.loc[mail_data['Category'] =='ham', 'Category',] =1

x = mail_data['Message']

y = mail_data['Category']

print(x)

print(y)

"""Splitting the data into training data and test data"""

x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=3)

print(x.shape)
print(x_train.shape)
print(x_test.shape)

"""Feature extraction """

# transform the text data to featurevectors that can be used as input to the logistic regression model
feature_extraction =TfidfVectorizer(min_df =1 , stop_words ='english' , lowercase ='True')

x_train_features = feature_extraction.fit_transform(x_train)
x_test_features = feature_extraction.transform(x_test)

y_train = y_train.astype('int')
y_test = y_test.astype('int')

print(x_train_features)

"""Training the machine learning model (logistic regression)"""

model= LogisticRegression()

#training the logistic regression model with the training data
model.fit(x_train_features, y_train)

"""Evaluating the trained model ->"""

prediction_on_training_data = model.predict(x_train_features)
accuracy_on_training_data = accuracy_score(y_train, prediction_on_training_data)

print('Accuracy on training data :' , accuracy_on_training_data)

prediction_on_test_data = model.predict(x_test_features)
accuracy_on_test_data = accuracy_score(y_test, prediction_on_test_data)

print('Accuracy on test data :' , accuracy_on_test_data)

"""Building  a predictive system ->

"""

input_mail=["As per your request 'Melle Melle (Oru Minnaminunginte Nurungu Vettam)' has been set as your callertune for all Callers. Press *9 to copy your friends Callertune"]
#convert text to feature vetors -
input_data_features = feature_extraction.transform(input_mail)

#making predicions 
prediction =model.predict(input_data_features)

#print(prediction)

if prediction[0]==1:
  print('ham mail')
else:
  print('spam mail')

input_mail=["SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info"]
#convert text to feature vetors -
input_data_features = feature_extraction.transform(input_mail)

#making predicions 
prediction =model.predict(input_data_features)

#print(prediction)

if prediction[0]==1:
  print('ham mail')
else:
  print('spam mail')

