# %%
import pandas as pd

# %%
# reading the database
data = pd.read_csv("students.csv")

# %%
# printing the top 10 rows
display(data.head(10))

# %%
# Show the dataset info
data.info()

# %%
# Missing Value Checking
data.isna().sum()

# %%
# Filling Nan Value with mode
data.fillna({'lunch': data['lunch'].mode()[0]}, inplace=True)

#%%
# Filling Nan Value with mean
data.fillna({'reading score': data['reading score'].mean()}, inplace=True)

# %%
# Filling Nan Value with mode
data.fillna({'grade': data['grade'].median()}, inplace=True)
# %%
# Check the information of the dataset
data.info()

# %%
# Interpolate the Missing Value
data['reading score'].interpolate(methode='linear', inplace=True)

# %%
# Interpolate the Missing Value
data['grade'].interpolate(methode='linear', inplace=True)

# %%
#backwardfill the missing value
data['lunch'].fillna(method='bfill', inplace=True)

# %%
#forwardfill the missing value
data['lunch'].fillna(method= 'bfill', inplace = True)

# %%
# drop Nan Value
data["lunch"].dropna(axis=0, inplace=True)

# drop feature with more than 50% are Nan value
data["lunch"].drop(axis=1, inplace=True)
