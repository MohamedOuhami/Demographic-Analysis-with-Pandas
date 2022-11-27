import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(
        "data/adult_data.csv",
        header = None,
        names=["age","workclass","fnlwgt","education","education-num","marital_status","occupation","relationship","race","sex","capital_gain","capital_loss","hours-per-week","native-country","salary"]
    )
    print(df['race'].unique())
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = {
        'white_race_count' : (df["race"] == "White").sum(),
        'black_race_count' : (df["race"] == "Black").sum(),
        'asian_race_count' : (df["race"] == "Asian-Pac-Islander").sum(),
        'indian_race_count' : (df["race"] == "Amer-Indian-Eskimo").sum(),
        'other_race_count' : (df["race"] == "Other").sum(),
    }


    # What is the average age of men?
    average_age_men = df['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').sum() / df['education'].count() * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    condition_df = df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == ">50K")]
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_education = df[(df['education'] != 'Bachelors') | (df['education'] != 'Masters') | (df['education'] != 'Doctorate')]
    
    # percentage with salary >50K
    higher_education_rich_df = higher_education[(higher_education['salary'] == ">50K")]
    lower_education_rich_df = lower_education[(lower_education['salary'] == ">50K")]
    higher_education_rich = higher_education_rich_df['age'].count() / df['education'].count() * 100
    lower_education_rich = lower_education_rich_df['age'].count() / df['education'].count() * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_min = df[(df['salary'] == '>50K')]
    min_workers = rich_min[(rich_min["hours-per-week"] == min_work_hours)]
    num_min_workers = min_workers['age'].count()

    rich_percentage = num_min_workers / df['education'].count() * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (rich_min['native-country'].mode())[0]
    united_states_rich = rich_min[(rich_min['native-country'] == 'United-States')]
    highest_earning_country_percentage = united_states_rich['age'].count() / df['education'].count() * 100

    # Identify the most popular occupation for those who earn >50K in India.
    indian_pop = df[(df['native-country'] == 'India')]
    rich_indian_pop = indian_pop[(indian_pop['salary'] == '>50K')]
    top_IN_occupation = (rich_indian_pop['occupation'].mode())[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()