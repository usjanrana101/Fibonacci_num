# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:58:09 2019
 Fibonacci by using Lambda 
@author: Jagannath
"""
fibo=lambda n:fibo(n-1)+fibo(n-2) if n>2 else 1
for i in range(1,100):
    print (fibo(i))
# this program takes too much time as for each n fibo function is called recursively