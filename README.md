# Analyzing Flight Data

This repository contains Python code for analyzing and visualizing flight data. The code uses the `pandas`, `matplotlib`, and `seaborn` libraries to perform exploratory data analysis and generate various plots to gain insights into flight prices, delays, and other factors.

## Data

The code uses a dataset named `flight.csv`. This dataset should contain information about flights, including the following columns:

* **coach_price:** The price of a coach ticket.
* **firstclass_price:** The price of a first-class ticket.
* **hours:** The duration of the flight in hours.
* **delay:** The flight delay in minutes.
* **inflight_meal:** Whether an in-flight meal is offered (Yes/No).
* **inflight_entertainment:** Whether in-flight entertainment is offered (Yes/No).
* **inflight_wifi:** Whether in-flight WiFi is offered (Yes/No).
* **day_of_week:** The day of the week of the flight.
* **redeye:** Whether the flight is a redeye flight (Yes/No).

Make sure to replace `'flight.csv'` with the actual path to your data file.

## Analysis

The code performs the following analysis:

**Task 1: Analyze coach prices**

* Creates a boxplot of coach prices.
* Creates a histogram of coach prices.

**Task 2: Analyze coach prices for 8-hour flights**

* Calculates and prints the mean and median coach prices for 8-hour flights.
* Creates a histogram of coach prices for 8-hour flights.

**Task 3: Analyze flight delays**

* Calculates and prints the mean, mode, and median flight delays.
* Creates a histogram of flight delays (excluding delays greater than 50 minutes).

**Task 4: Analyze relationship between coach and first-class prices**

* Creates a scatter plot with a fitted regression line (using LOWESS smoothing) to visualize the relationship between coach prices and first-class prices (using a 10% sample of the data).

**Task 5: Analyze coach prices by in-flight amenities**

* Creates histograms and boxplots of coach prices grouped by in-flight meal, entertainment, and WiFi options.

**Task 6: Visualize relationship between flight length and passengers**

* Creates a scatter plot of the number of passengers vs. flight length, with jitter added to reduce overplotting.

**Task 7: Visualize coach vs. first-class prices by day of the week**

* Creates a scatter plot of coach prices vs. first-class prices, with color-coding by day of the week (using a 10% sample of the data).

**Task 8: Analyze coach prices by day of the week and redeye status**

* Creates a boxplot of coach prices grouped by day of the week and redeye status (using a 10% sample of the data).

## Usage

1. Make sure you have the necessary libraries installed (`pandas`, `numpy`, `matplotlib`, and `seaborn`). You can install them using `pip install pandas numpy matplotlib seaborn`.
2. Place your `flight.csv` data file in the same directory as the Python script.
3. Run the Python script.

## Output

The code will produce various plots and statistics that provide insights into the flight data.

## Contributing

Feel free to fork this repository and contribute your own improvements or modifications.

## License

This code is released under the MIT License.
