Level 1 TASK 1
------------------------------------------------------------------------

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Dataset .csv') #importing dataset

df #printing dataset

df.info #Identifying number of rows and columns

df.notnull() #Identifying the missing values present in each row

df = df.astype({'Aggregate rating': 'int'}) #Data type conversation
sns.distplot(df['Aggregate rating'], bins=10) #Analyze representation of the normal variable
plt.show() #check for class imbalances
sns.countplot(df)
plt.show()

------------------------------------------------------------------------

Level 1 TASK 2

import pandas as pd
df = pd.read_csv('/content/Dataset .csv')
numerical_stats = df.describe() # Calculating basic statistics for numerical columns
print(numerical_stats)

statistic_measures ={} #Initializing a row to store all the variables data

#apply for each variable column
for column in numerical_stats:
#fetch the record for the next column
   values = df[column].values
#calculate basic stats
mean = np.mean(values)
median = np.median(values)
standard_deviation = np.std(values)
#store the calculated result
statistic_measures[column] = {
'Mean':mean,
      'Median':median,
      'Standard Deviation': standard_deviation,
  }
#print the statistical measures for each numerical column
for column, measures in statistic_measures.items():
            print(f'Column_name:{column}')
for measure, value in measures.items():
            print(f'{measures}:{values}')
            print(':' * 50)

country_code_counts = df['Country Code'].value_counts() # Explore the distribution of "Country Code"
print(country_code_counts)

city_counts = df['City'].value_counts() # Explore the distribution of "City"
print(city_counts)
cuisines_counts = df['Cuisines'].value_counts() # Explore the distribution of "Cuisines"
print(cuisines_counts)

top_cities = city_counts.head(10) # Top cities with the highest number of restaurants
print(top_cities)

------------------------------------------------------------------------

Level 1 TASK 3

import pandas as pd
import matplotlib.pyplot as plt
import folium
df = pd.read_csv('/content/Dataset .csv')
# Visualization the locations of restaurants on a map using latitude and longitude information.
restaurant_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=6)
for index, row in df.iterrows():
    popup_text = f"{row['Restaurant Name']} - Rating: {row['Votes']}"
    folium.Marker([row['Latitude'], row['Longitude']], popup=popup_text).add_to(restaurant_map)
restaurant_map.save('restaurant_map.html')
# Analyze the distribution of restaurants across different cities
city_distribution = df['City'].value_counts()
# Plot the distribution using a bar chart
plt.bar(city_distribution.index, city_distribution.values)
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.title('Restaurant Distribution across Cities')
plt.xticks(rotation=45)
plt.show()
# Plotting scatter plot with size based on rating
plt.scatter(df['Longitude'], df['Latitude'], s=df['Votes'] * 20, alpha=0.7)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Restaurant Locations and Ratings')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/content/Dataset .csv')
city_country_counts = df["City"].value_counts()
# Plot the distribution of restaurants across cities or countries
plt.figure(figsize=(15, 6))
sns.barplot(x=city_country_counts.index, y=city_country_counts.values)
plt.xticks(rotation=90)
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Restaurants across Cities/Countries")
plt.show()
# Checking the correlation between restaurant's location with latitude, longitude and its rating
correlation = df[["Latitude", "Longitude", "Cuisines"]].corr()
# Plot the correlation matrix using a heatmap
plt.figure(figsize=(6, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation between Restaurant's Location and Rating")
plt.show()
