import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('population.csv', skiprows=4)

# Clean and prepare population data for 2022
df_2022 = df[['Country Name', '2022']].dropna()
df_top10 = df_2022.sort_values(by='2022', ascending=False).head(10)

sns.set(style="whitegrid")

# ----------------------- Bar Chart: Top 10 Countries -----------------------
plt.figure(figsize=(12, 6))
barplot = sns.barplot(data=df_top10, x='2022', y='Country Name', palette='viridis')
plt.title('Top 10 Countries by Population in 2022')
plt.xlabel('Population')
plt.ylabel('Country')

# Annotate bars
for index, row in df_top10.iterrows():
    plt.text(row['2022'] + 1e7,              
             index - df_top10.index[0],      
             f"{int(row['2022']):,}",       
             va='center', fontsize=9, color='black')

plt.tight_layout()
plt.show()

# ----------------------- Histogram: Distribution -----------------------
plt.figure(figsize=(12, 6))
hist = sns.histplot(df_2022['2022'], bins=30, kde=True, color='orange')

# Mean and Median lines
mean_val = df_2022['2022'].mean()
median_val = df_2022['2022'].median()
plt.axvline(mean_val, color='blue', linestyle='--', label=f'Mean: {mean_val:,.0f}')
plt.axvline(median_val, color='red', linestyle='--', label=f'Median: {median_val:,.0f}')

plt.title('Distribution of Population Across Countries (2022)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.legend()
plt.tight_layout()
plt.show()

# ----------------------- Line Plot: India Population Over Time -----------------------
df_india = df[df['Country Name'] == 'India'].dropna(axis=1)
years = df_india.columns[4:]  # Year columns
india_pop = df_india.iloc[0, 4:].astype(float)

plt.figure(figsize=(12, 6))
plt.plot(years, india_pop, marker='o', color='green', linewidth=2)
plt.title('India Population Growth (1960 - 2022)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------- Bar Chart: South Asian Countries -----------------------
south_asia = ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 'Bhutan', 'Maldives', 'Afghanistan']
df_south = df_2022[df_2022['Country Name'].isin(south_asia)].sort_values(by='2022', ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=df_south, x='2022', y='Country Name', palette='magma')
plt.title('Population of South Asian Countries in 2022')
plt.xlabel('Population')
plt.ylabel('Country')

# Annotate bars
for index, row in df_south.iterrows():
    plt.text(row['2022'] + 1e6,
             index - df_south.index[0],
             f"{int(row['2022']):,}",
             va='center', fontsize=9, color='black')

plt.tight_layout()
plt.show()
