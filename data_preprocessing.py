# Data Preprocessing

# Importing the Libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the Dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values
    # x are independent variables
    # y is the dependent variable
# Missing Data: Taking care of it
from sklearn.preprocessing import Imputer
    # sklearn is a giant library with helpful ML tools
    # preprocessing is package that helps with preprocessing datasets 
    # Imputer is a class that helps to take care of missing data
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[:,1:3]) #using imputer on the second & third column, upperbound is excluded that is why its 3 instead of 2 (ending at two and not going to 3)
x[:,1:3] = imputer.transform(x[:,1:3])

# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    # LabelEncoder is a class that changes the categorical variables into a hierarchy of numeric values
    # OneHotEncoder is a class that creates dummy variables
# Encode country column
labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0]) # 0 represents the index for the country column
x = onehotencoder.fit_transform(x).toarray()
# Encode purchase column
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting dataset into test and train
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
    # random_state is like setting the seed 
    # test_size 0.2 means that the test set contains 20% of the dataset

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)




















