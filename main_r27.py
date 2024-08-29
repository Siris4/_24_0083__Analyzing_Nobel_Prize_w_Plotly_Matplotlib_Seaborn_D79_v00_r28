import pandas as pd

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'birth_country_current' and 'year', and count the number of prizes won
country_year_counts = df.groupby(['birth_country_current', 'year']).size().reset_index(name='prizes_won')

# Sum the total number of prizes won by each country
total_prizes_by_country = country_year_counts.groupby('birth_country_current')['prizes_won'].sum()

# Sort by the total number of prizes won in descending order and select the top 20 countries
top20_countries_list = total_prizes_by_country.sort_values(ascending=False).index[:20]

# Filter the DataFrame to include only the top 20 countries, sorted by the highest total number of prizes
top20_countries = country_year_counts[country_year_counts['birth_country_current'].isin(top20_countries_list)]

# Sort the filtered DataFrame by 'prizes_won' from highest to lowest
top20_countries = top20_countries.sort_values(by='prizes_won', ascending=False)

# Display the resulting DataFrame
print(top20_countries)
