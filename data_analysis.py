
minimum = 9999
minimum_country = ''
minimum_year = 0
maximum = 0
maximum_country = ''
maximum_year = 0

age_list = []
spec_min_age = 9999
spec_min_country = ''
spec_max_age = 0
spec_max_country = ''

selected_year = int(input('Please, enter year of interest: ').strip())

with open('life-expectancy.cvs') as le:
    for i, line in enumerate(le):
        if i == 0:
            continue

        line = line.strip()
        data = line.split(',')
        country = data[0]
        year = int(data[2])
        age = float(data[3])

        if age < minimum:
            minimum = age
            minimum_country = country
            minimum_year = year

        if age > maximum:
            maximum = age
            maximum_country = country
            maximum_year = year

        if year == selected_year:
            age_list.append(age)

            if age < spec_min_age:
                spec_min_age = age 
                spec_min_country = country
            if age > spec_max_age:
                spec_max_age = age
                spec_max_country = country

spec_avg = sum(age_list) / len(age_list)

print(f'\nThe overoll max life expectancy is: {maximum} from {maximum_country} in {maximum_year}')
print(f'\nThe overoll min life expectancy is: {minimum} from {minimum_country} in {minimum_year}')

print(f'\nFor the year {selected_year}:')