# Data Preprocessing

# Importing the dataset
dataset = read.csv('Data.csv')

# Missing Data: Taking care of it
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)

# Encoding Categorical Data
dataset$Country = factor(dataset$Country,
                         levels = c('France','Spain','Germany'),
                         labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c('No','Yes'),
                           labels = c(0,1))

# Splitting the data into training and testing sets
# install.packages('caTools')
  # Firewall at work blocked package installation
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased,
                     SplitRatio = 0.8) 
  # 0.8 means that the testing set contains 20% of the dataset
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set = scale(training_set)
test_set = scale(test_set)
  # Error: 'x must be numeric'
  # Reason: Country and Purchased columns are factors
  # Solution: Don't apply feature scaling to those columns
training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])

