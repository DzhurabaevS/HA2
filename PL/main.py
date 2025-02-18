import pandas as pd
import numpy as np

# 1- list, tuple, dictionary, NumPy array, scalar, and Pandas Series objects.

# 2
months = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                   index=['january', 'february', 'mart', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'])
print(months)

# 3
groups = {'MatMIE': 30, 'Mat DAIS': 25, 'COMIE': 40, 'COMEC': 35}
students_series = pd.Series(groups)
print(students_series)

# 4
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print(df)

# 5
filtered_df = df[df['attempts'] > 2]
print(filtered_df)
