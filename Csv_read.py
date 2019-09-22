#!/usr/bin/env python
# coding: utf-8

import pandas as pd
df = pd.read_csv('new.csv', encoding = 'cp1251', delimiter=';', index_col=False)

brands = df['Бренд'].unique()

for brand in brands:
    file_name = brand + ".csv"
    new_files = df[df['Бренд']==brand]
    new_files.to_csv(file_name, index=False, encoding='cp1251')


