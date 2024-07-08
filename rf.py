
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import sys


filename = 0## your csv file


# Check if the file is a CSV file
if not filename.endswith('.csv'):
    print("File format is not expected. Choose a CSV file always.")
    sys.exit()

# Check if the input and output columns are in the proper format
try:
    input_column = [1,2,3,4,5,6,7,8,9]
    output_column = [10]
except ValueError:
    print("Improper format for input or output column.")
    sys.exit()


# Load the CSV file
try:
    data = pd.read_csv(filename)
    print("Total number of Rows : "+str(len(data)))
except FileNotFoundError:
    print(f"File {filename} not found.")
    sys.exit()

# Extract the input and output data
X = data.iloc[:, input_column].values
y = data.iloc[:, output_column].values
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create the Random Forest model
try:
    model = RandomForestRegressor(n_estimators=100, random_state=42, verbose=2,
                                  n_jobs=20)
except ValueError:
    print("Invalid value for number of estimators or number of jobs.")
    sys.exit()

# Train the model
if len(X_train) == len(y_train.ravel()):
    model.fit(X_train, y_train.ravel())
else:
    model.fit(X_train, y_train)

# Predict the output
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print("Mean Squared Error is:", mse)
print("Mean Absolute Error is:", mae)

# Save the model
joblib.dump(model, filename+'model.joblib')
