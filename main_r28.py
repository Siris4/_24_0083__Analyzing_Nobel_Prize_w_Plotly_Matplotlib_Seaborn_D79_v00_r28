import pandas as pd

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'birth_country_current' and 'year', and count the number of prizes won
country_year_counts = df.groupby(['birth_country_current', 'year']).size().reset_index(name='prizes_won')

# Sort by the number of prizes won in descending order
sorted_country_year_counts = country_year_counts.sort_values(by='prizes_won', ascending=False)

# Select the top 20 entries
top20_countries = sorted_country_year_counts.head(20)

# Display the resulting DataFrame
print(top20_countries)
