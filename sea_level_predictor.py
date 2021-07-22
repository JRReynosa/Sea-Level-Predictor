import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 9))

    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line_one = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    series_one = df['Year'].append(pd.Series(range(2014,2051)))
    plt.plot(series_one, (line_one.intercept + line_one.slope*series_one))

    # Create second line of best fit
    df = df.loc[df['Year'] >= 2000]
    line_two = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    series_two = df['Year'].append(pd.Series(range(2014,2051)))
    plt.plot(series_two, (line_two.intercept + line_two.slope*series_two))

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()