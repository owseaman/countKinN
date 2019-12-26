# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:46:26 2019

@author: Owoeye
"""

#k = 2
#k = str(k)
#n = 35

def countKinN(k, n):
    
    #k = int(input('enter k...'))
    #n = int(input('enter n...'))
    
    lst = []
            #newCount = 0
            #maxiCount = int(count)
    try:        
            for number in range(0, n+1):
                lst.append(number)
                #print(numbers, number, count)
                #print(str(lst))
                numbers = str(lst)
            #print(numbers, type(numbers))
            count = numbers.count(str(k))
            print(count)
            
    except:
            print("Error!!! \nEnter an Integer")