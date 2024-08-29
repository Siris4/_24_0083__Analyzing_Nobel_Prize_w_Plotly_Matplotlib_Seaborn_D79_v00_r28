import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Count the number of prizes awarded each year
prizes_per_year = df['year'].value_counts().sort_index()

# Calculate the 5-year rolling average for the number of prizes
rolling_avg = prizes_per_year.rolling(window=5).mean()

# Convert the 'prize_share' fraction to a numerical value
df['prize_share_numeric'] = df['prize_share'].apply(lambda x: eval(x))

# Convert the numerical value to a percentage
df['prize_share_percentage'] = df['prize_share_numeric'] * 100

# Calculate the average prize share percentage for each year
average_prize_share_per_year = df.groupby('year')['prize_share_percentage'].mean()

# Calculate the 5-year rolling average of the percentage share
rolling_avg_percentage_share = average_prize_share_per_year.rolling(window=5).mean()

# Create the figure and set the size and DPI
plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year and Prize Share Percentage', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5), fontsize=14, rotation=45)

# Get the current axis and create a secondary axis
ax1 = plt.gca()
ax2 = ax1.twinx()

# Set x-axis limits
ax1.set_xlim(1900, 2020)

# Invert the secondary y-axis
ax2.invert_yaxis()

# Plot the scatter plot (matching the flow of the number of prizes)
ax1.scatter(x=prizes_per_year.index,
            y=rolling_avg.values,  # Match scatter plot with the 5-year rolling average line
            c='dodgerblue',
            alpha=0.7,
            s=100)

# Plot the 5-year rolling average of the number of prizes (line plot)
ax1.plot(rolling_avg.index,
         rolling_avg.values,
         c='crimson',
         linewidth=3,
         label='5-Year Rolling Avg (Number of Prizes)')

# Plot the 5-year rolling average of the prize share percentage on the secondary axis (line plot)
ax2.plot(rolling_avg_percentage_share.index,
         rolling_avg_percentage_share.values,
         c='grey',
         linewidth=3,
         label='5-Year Rolling Avg % (Prize Share)')

# Add the legend
fig = plt.gcf()
fig.legend(loc='upper left', bbox_to_anchor=(0.1,0.9))

# Adjust layout to ensure everything fits without overlap
fig.tight_layout()

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prizes_combined_plot.png"
plt.savefig(output_path)

# Since plt.show() is not needed for saving, we can omit it
