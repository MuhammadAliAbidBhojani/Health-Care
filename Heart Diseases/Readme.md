# Heart Diseases
This is a small project to import, clean and analyse Heart Disease Data

# Data Preparation 
```python
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
```

# Data Visualization

First. Lets take a look at the Age Distribution among heart patients:
!['Age Distribution'](Age%20Histogram.png)

It seems that a majority of patients in the dataset were in their 50s

But does it make them more likely to get Heart Diseases?

Lets look at how the Age Group Effects the Blood Pressure:
!['BP per Age Group'](Age-Group%20per%20BP%20Levels.png)

Lets also take a look at the Cholesterol Levels per Age Groups:
!['Cholesterol levels per Age Group'](Chol%20Levels%20per%20Age-Group.png)

It seems people in their 50s have higher BP and Cholesterol Levels on average.
But does it mean they have a higher risk factor?

!['Risk Factor per Age Group'](Risk%20Factor%20per%20Age-Group.png)

It seems even though the 50s Age Group has higher BP and Cholesterol on Average. It doesnt put them at a higher risk factor overall.

It can also be seen that as the Age increases the Risk Factor also increases. 

Lets also take a look at the more common type of Chest Pain experienced by the Patients
!['CP Type by Patients'](Number%20of%20Patients%20per%20CP-Type.png)

Finally. Lets see which gender is more likely to have Heart Diseases:
!['Number of Patients per Gender'](Patients%20per%20Gender.png)

It seems the majority of Patients in the Dataset were Male,
while only 32.42% Patients were Female