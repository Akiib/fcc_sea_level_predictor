import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'],c='r', marker= '.')

    # Create first line of best fit

    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xA = np.arange(df['Year'].min(),2051,1)
    yA = xA*line1.slope + line1.intercept

    plt.plot(xA,yA)
    # Create second line of best fit
    df_2 = df[df['Year']>=2000]

    line2 = linregress(df_2['Year'],df_2['CSIRO Adjusted Sea Level'])
    
    xB = np.arange(2000,2051,1)
    yB = xB*line2.slope + line2.intercept
    
    plt.plot(xB,yB)

    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()