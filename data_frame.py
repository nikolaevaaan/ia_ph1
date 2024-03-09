import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение One-Hot Encoding для столбца 'whoAmI'
one_hot_encoding = pd.get_dummies(data['whoAmI'])

# Объединение исходного DataFrame с DataFrame One-Hot Encoding
one_hot_data = pd.concat([data, one_hot_encoding], axis=1)

# Удаление исходного столбца 'whoAmI'
one_hot_data.drop('whoAmI', axis=1, inplace=True)

# Вывод первых строк преобразованных данных
print(one_hot_data.head())