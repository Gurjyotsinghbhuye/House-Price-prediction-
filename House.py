import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Dataframe = pd.read_csv(r'C:\Users\karan\Desktop\Practice\spotify\Housing\Housing.csv')
house=pd.DataFrame(Dataframe)

# print(house.head(20))
print(house.info())
print(house.describe())

check_nan=house[house.isna()]
print(check_nan)

sns.pairplot(house[['price', 'area', 'bedrooms', 'bathrooms']])
plt.show()

# Step 3: Data Preprocessing
# Handle Missing Values:

# Handle missing data by either removing rows with missing values or filling them with the median/mean of the column.

# house.fillna(house.median(), inplace=True)
