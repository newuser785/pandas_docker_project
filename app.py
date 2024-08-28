import pandas as pd

# Загрузка данных из CSV-файла
df = pd.read_csv('data.csv')

# Просмотр первой строки данных
print(df.head())

# Анализ данных
average_salary = df['salary'].mean()
filtered_df = df[df['age'] > 30]

print(f'Средняя зарплата: {average_salary:.2f}')
print(f'Сотрудники старше 30 лет:\n{filtered_df.to_string(index=False)}')
