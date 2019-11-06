# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 02:24:41 2019
 Take n as argument and return first n fibonacci numbers
@author: Jagannath
"""
def fibo_n(n):
    f=[]
    for i in range(n):
            if i==0:
                f.append(1)
            elif i==1:
                f.append(1)    
            else:
                f.append(f[i-2]+f[i-1])
    return(f)                

 
 
