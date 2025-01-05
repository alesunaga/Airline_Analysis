# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data
flight = pd.read_csv("flight.csv")
print(flight.head())

# Task 1: Analyze coach prices
# Create a boxplot of coach prices
plt.boxplot(flight.coach_price)
plt.title('Boxplot of Coach Prices')
plt.ylabel('Price')
plt.show()
plt.clf()

# Create a histogram of coach prices
plt.hist(flight.coach_price)
plt.title('Histogram of Coach Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()
plt.clf()

# Task 2: Analyze coach prices for 8-hour flights
print("Mean coach price for 8-hour flights:", np.mean(flight.coach_price[flight.hours == 8]))
print("Median coach price for 8-hour flights:", np.median(flight.coach_price[flight.hours == 8]))

sns.histplot(flight.coach_price[flight.hours == 8])
plt.title('Histogram of Coach Prices for 8-hour Flights')
plt.xlabel('Price')
plt.show()
plt.clf()

# Task 3: Analyze flight delays
print("Mean flight delay:", flight.delay.mean())
print("Mode of flight delay:", flight.delay.mode())
print("Median flight delay:", flight.delay.median())

sns.histplot(flight.delay[flight.delay < 50])  # Filter out extreme delays for better visualization
plt.title('Histogram of Flight Delays (less than 50)')
plt.xlabel('Delay (minutes)')
plt.show()
plt.clf()

# Task 4: Analyze relationship between coach and first-class prices
# Create a 10% sample of the DataFrame
flight_sample = flight.sample(frac=0.1, random_state=42)

sns.lmplot(x="coach_price", y="firstclass_price", data=flight_sample, line_kws={'color': 'black'}, lowess=True)
plt.title('Coach Price vs. First Class Price (10% Sample)')
plt.xlabel('Coach Price')
plt.ylabel('First Class Price')
plt.show()
plt.clf()

# Task 5: Analyze coach prices by in-flight amenities
# Histograms of coach prices by in-flight amenities
sns.histplot(data=flight, x='coach_price', hue='inflight_meal', multiple='stack')
plt.title('Coach Prices with In-flight Meal')
plt.show()
plt.clf()

sns.histplot(data=flight, x='coach_price', hue='inflight_entertainment', multiple='stack')
plt.title('Coach Prices with In-flight Entertainment')
plt.show()
plt.clf()

sns.histplot(data=flight, x='coach_price', hue='inflight_wifi', multiple='stack')
plt.title('Coach Prices with In-flight WiFi')
plt.show()
plt.clf()

# Boxplots of coach prices by in-flight amenities
sns.boxplot(x='inflight_meal', y='coach_price', data=flight)
plt.title('Coach Prices by In-flight Meal')
plt.show()
plt.clf()

sns.boxplot(x='inflight_entertainment', y='coach_price', data=flight)
plt.title('Coach Prices by In-flight Entertainment')
plt.show()
plt.clf()

sns.boxplot(x='inflight_wifi', y='coach_price', data=flight)
plt.title('Coach Prices by In-flight WiFi')
plt.show()
plt.clf()

# Task 6: Visualize relationship between flight length and passengers
# Add jitter to the 'hours' and 'passengers' data
jittered_hours = flight['hours'] + np.random.normal(0, 0.1, size=flight.shape[0])
jittered_passengers = flight['passengers'] + np.random.normal(0, 5, size=flight.shape[0])

# Scatter plot with jitter
plt.scatter(jittered_hours, jittered_passengers, alpha=0.5)
plt.title('Number of Passengers vs. Flight Length (with Jitter)')
plt.xlabel('Flight Length (hours)')
plt.ylabel('Number of Passengers')
plt.show()
plt.clf()

# Task 7: Visualize coach vs. first-class prices by day of the week
# Create a mapping from day names to numeric codes
day_mapping = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}

# Map the day names to numeric codes
day_codes = flight_sample.day_of_week.map(day_mapping)

# Create the scatter plot with color-coding using the numeric codes
plt.scatter(flight_sample.coach_price, flight_sample.firstclass_price, c=day_codes, cmap='viridis')

# Set plot labels and title
plt.title('Coach Price vs. First Class Price by Day of Week (10% Sample)')
plt.xlabel('Coach Price')
plt.ylabel('First Class Price')

# Add a colorbar to show the day of the week mapping
plt.colorbar(label='Day of Week')

# Show the plot
plt.show()
plt.clf()

# Task 8: Analyze coach prices by day of the week and redeye status
# Boxplot of coach prices by day of the week, with hue for redeye
# Define the order of the days of the week
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sns.boxplot(x='day_of_week', y='coach_price', hue='redeye', data=flight_sample, order=days_order)
plt.title('Coach Prices by Day of the Week and Redeye Status (10% Sample)')
plt.xlabel('Day of the Week')
plt.ylabel('Coach Price')
plt.show()
plt.clf()
