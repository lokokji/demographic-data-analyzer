import pandas as pd

data = pd.read_csv('adult.csv')

race_count = data['race'].value_counts()
print("Jumlah orang berdasarkan ras:")
print(race_count)

average_age_men = data[data['sex'] == 'Male']['age'].mean()
print("Rata-rata usia pria:", round(average_age_men, 1))

bachelors_percentage = (data['education'] == 'Bachelors').mean() * 100
print("Persentase orang yang memiliki gelar sarjana:", round(bachelors_percentage, 1))

higher_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
higher_education_salary = data[higher_education & (data['salary'] == '>50K')].shape[0]
higher_education_total = higher_education.sum()
higher_education_percentage = (higher_education_salary / higher_education_total) * 100
print("Persentase orang dengan pendidikan tinggi yang memiliki gaji lebih dari 50K:", round(higher_education_percentage, 1))

no_higher_education = ~higher_education
no_higher_education_salary = data[no_higher_education & (data['salary'] == '>50K')].shape[0]
no_higher_education_total = no_higher_education.sum()
no_higher_education_percentage = (no_higher_education_salary / no_higher_education_total) * 100
print("Persentase orang tanpa pendidikan tinggi yang memiliki gaji lebih dari 50K:", round(no_higher_education_percentage, 1))

min_hours_per_week = data['hours-per-week'].min()
print("Jumlah jam minimum yang bekerja per minggu:", min_hours_per_week)

min_hours_people = data[data['hours-per-week'] == min_hours_per_week]
min_hours_salary_percentage = (min_hours_people['salary'] == '>50K').mean() * 100
print("Persentase orang yang bekerja dengan jam minimum yang memiliki gaji lebih dari 50K:", round(min_hours_salary_percentage, 1))

earning_50k_data = data[data['salary'] == '>50K']
if not earning_50k_data.empty:
    highest_earning_country = earning_50k_data['native-country'].value_counts().idxmax()
    highest_earning_country_percentage = (earning_50k_data[earning_50k_data['native-country'] == highest_earning_country].shape[0] / earning_50k_data.shape[0]) * 100
    print(f"Negara dengan persentase tertinggi yang menghasilkan >50K adalah {highest_earning_country} dengan persentase {round(highest_earning_country_percentage, 1)}")
else:
    print("Tidak ada data dengan penghasilan lebih dari 50K.")


india_occupation_data = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
if not india_occupation_data.empty:
    india_occupation = india_occupation_data['occupation'].mode()
    if not india_occupation.empty:
        india_occupation = india_occupation[0]
        print(f"Pekerjaan yang paling populer di India untuk orang dengan gaji lebih dari 50K adalah {india_occupation}.")
    else:
        print("Tidak ada pekerjaan dengan gaji lebih dari 50K di India.")
else:
    print("Tidak ada data orang dari India dengan gaji lebih dari 50K.")
