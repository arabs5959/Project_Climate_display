import pandas as pd #read CSV file
import matplotlib.pyplot as plt #making the plot
import seaborn as sns #Making it look nice
import matplotlib.dates as mdates #making the best fit line
import numpy as np #displaying the equation of the best fit line

# reading the data from the CSV file
df = pd.read_csv('climate.csv')

# converting the 'Date/Time' column to datetime format
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Making it the right size 
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# making average temp
df['Avg_Temp'] = (df['Max Temp (°C)'] + df['Min Temp (°C)']) / 2

# This removes rows where 'Avg_Temp' or 'Date/Time' are blank so the math doesn't break
df = df.dropna(subset=['Date/Time', 'Avg_Temp'])

# Convert datetime to numeric values so regplot and polyfit can calculate the trend line math
x_numeric = mdates.date2num(df['Date/Time'])

# polyfit should wplr now
slope, intercept = np.polyfit(x_numeric, df['Avg_Temp'], 1)

# Format the equation string nicely
equation_text = f'Equation: y = {slope:.4f}x + {intercept:.2f}'


# sns.regplot handles BOTH the scatter dots and the trend line automatically
sns.regplot(
    x=x_numeric, 
    y=df['Avg_Temp'], 
    color='crimson', 
    scatter_kws={'alpha': 0.6, 's': 30, 'label': 'Daily Avg Temp'},  # Customizes the scatter points
    line_kws={'color': 'black', 'linewidth': 2.5, 'label': equation_text} # Put equation in legend
)


# Define 'ax' here so it can be used for formatting and text positioning
ax = plt.gca() 

# Fix the X-axis labels back to readable dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.title('Average Daily Temperature Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)


# legend to show what the points and line mean
plt.legend(loc='upper right')

# Floating text box on the graph
plt.text(
    0.05, 0.95, equation_text, 
    transform=ax.transAxes, 
    fontsize=12, 
    fontweight='bold',
    verticalalignment='top', 
    bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8)
)

# Actually making it show
plt.tight_layout()
plt.show()

