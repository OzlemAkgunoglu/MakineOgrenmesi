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

veriler = pd.read_csv('veriler.csv')
print(veriler)

#verilerin ön işlenmesi

boy= veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)