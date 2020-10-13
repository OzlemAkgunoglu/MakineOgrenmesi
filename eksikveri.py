# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:18:37 2020

@author: einst
"""

#pandas kütüphanesi veriyi yüklemek için kullanılır.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#verilerin yüklenmesi

veriler = pd.read_csv('eksikveriler.csv')
print(veriler)

#eksik veriler
#sci kit learn

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
#iloc integer location
Yas= veriler.iloc[:,1:4].values
print(Yas)
imputer=imputer.fit(Yas[:,1:4])

Yas[:,1:4]= imputer.transform(Yas[:,1:4])
print(Yas)
