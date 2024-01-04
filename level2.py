Level 2 TASK 1

------------------------------------------------------------------------

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import glob
csv_files = glob.glob('*.csv') # Get a list of all CSV files in the current directory
with open(csv_files[0]) as f: # Open the first CSV file in the list
    data = f.read() # Read the data from the file

df=pd.read_csv('/content/Dataset .csv') #printing dataset

import pandas as pd
df=pd.read_csv('/content/Dataset .csv')
# Determine the percentage of restaurants that offer table booking and online delivery
table_booking_percentage = df['Has Table booking'].value_counts(normalize=True) * 100
online_delivery_percentage = df['Has Online delivery'].value_counts(normalize=True) * 100
print(f"Percentage of restaurants offering table booking:")
print(table_booking_percentage)
print(f"Percentage of restaurants offering online delivery:")
print(online_delivery_percentage)

city_percentage = df['City'] =='Yes' #calculate the percentage for city
print("percentage of city:", city_percentage)

# Compare the average ratings of restaurants with table booking and those without
average_rating_with_table_booking = df[df['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
average_rating_without_table_booking = df[df['Has Table booking'] == 'No']['Aggregate rating'].mean()
print(f"Average rating of restaurants with table booking: {average_rating_with_table_booking:.2f}")
print(f"Average rating of restaurants without table booking: {average_rating_without_table_booking:.2f}")

# Analyze the availability of online delivery among restaurants with different price ranges
online_delivery_by_price_range = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack() * 100
print("Percentage of restaurants offering online delivery by price range:")
print(online_delivery_by_price_range)

# plot the availability of online delivery by price range
online_delivery_by_price_range.plot(kind='bar')
plt.xlabel('Price Range')
plt.ylabel('percentage of restuarants')
plt.title('Availability of Online Delivery among different price Range')
plt.show()

------------------------------------------------------------------------

Level 2 TASK 2

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/Dataset .csv')
# Determining the most common price range among all the restaurants.
most_common_price_range = df['Price range'].mode().iloc[0]
print(f"Most Common Price Range : {most_common_price_range}")

# Calculating the average rating for each price range.
average_rating_by_price_range = df.groupby('Price range')['Votes'].mean()
print("Average Rating by Price Range:")
print(average_rating_by_price_range)

# Identifying the colour that represents the highest average rating among different price ranges
highest_rating_color=average_rating_by_price_range.idxmax()
print(f'color representing the highest average rating: {highest_rating_color}')

# Plotting the average rating by price range
average_rating_by_price_range.plot(kind='bar')
plt.xlabel('Price range')
plt.ylabel('Aggregate rating')
plt.title('Average Rating by Price Range')
plt.show()

------------------------------------------------------------------------

Level 2 TASK 3

#calculating the height of the restraurant name
df['Restaurant Name height'] = df['Restaurant Name']
#calculate the breadth and length of the locality
df['locality length and breadth'] = df['Locality']
#display the updated dataframe with additional features
print(df)

import pandas as pd
df=pd.read_csv('/content/Dataset .csv')
# Extracting additional features from the existing columns, such as the length of the restaurant name or address.
df['NameLength'] = df['Restaurant Name'].apply(len)
# Create new features like "Has Table Booking" or "Has Online Delivery" by encoding categorical variables.
df['Has Table booking'] = df['Has Table booking'].map({True: 1, False: 0})
df['Has Online delivery'] = df['Has Online delivery'].map({True: 1, False: 0})
print(df)
