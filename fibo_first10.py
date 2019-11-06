# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 01:16:14 2019
 Print first 10 fibonacci number
@author: Jagannath
""
import timeit
f=[]
for i in range(10):
    if i==0:
        f.append(1)
    elif i==1:
        f.append(1)    
    else:
        f.append(f[i-2]+f[i-1])
print (f)  
print(timeit.timeit())
