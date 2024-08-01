# importing Package
import pandas as pd

# Importing Heart Disease Data
heart_disease = pd.read_csv(
    'heart_disease_data_with_features.csv'
)

# Checking for missing values
print(heart_disease.isna().sum())

# Dropping the missing values
heart_disease = heart_disease.dropna()

# Converting the "sex" column from int to category
sex_map = {
    1: 'Male',
    0: 'Female'
}

heart_disease['sex'] = heart_disease['sex'].map(sex_map)
heart_disease['sex'] = heart_disease['sex']\
    .astype('category')

# Creating a cp_type column using the "cp" column
cp_map = {
    1: 'Typical Angina',
    2: 'Atypical Angina',
    3: 'Non-Anginal Pain',
    4: 'Asymptomatic'
}

heart_disease['cp_type'] = heart_disease['cp'].map(cp_map)

# Converting to Category
heart_disease['cp_type'] = heart_disease['cp_type']\
    .astype('category')

# Creating a restecg_type column using the "restecg" column
ecg_map = {
    0: 'Normal',
    1: 'ST-T Wave Abnormality',
    2: 'Left Ventricular Hypertrophy'
}

heart_disease['restecg_type'] = heart_disease['restecg'].map(ecg_map)

# Converting to Category
heart_disease['restecg_type'] = heart_disease['restecg_type']\
    .astype('category')

# Creating a slope_type column using the "slope" column
slope_map = {
    1: 'Upsloping',
    2: 'Flat',
    3: 'Downsloping'
}

heart_disease['slope_type'] = heart_disease['slope'].map(slope_map)

# Converting to category
heart_disease['slope_type'] = heart_disease['slope_type']\
    .astype('category')

# Saving Data as a csv for Analysis
heart_disease.to_csv('Heart Disease Dataset.csv')