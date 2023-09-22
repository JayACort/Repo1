# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:16:41 2023

@author: Jermaine Cort
"""

import numpy

def simpleadd(a, b):
    return a+b

simpleadd(4, 5)

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

fibonacci(8)

for n in range(10):
    print(fibonacci(n))