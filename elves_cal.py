# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:47:23 2022

@author: CarDiDA
"""

elves_file = open('elves_calories.txt', 'r')

No_Elve = 1
Highest_Cal = 0
Cal_Sum = 0

for line in elves_file:
    
    if line < "1":
        print(No_Elve, " ", Cal_Sum)
        Cal_Sum = 0
        No_Elve += 1
            
    else:
        try:
            Cal_Sum += int(line)    

        except ValueError:
            pass
    
    if Cal_Sum > Highest_Cal:
        Highest_Cal = Cal_Sum
        First_Elve = No_Elve

        
print("Elve ", First_Elve, " with ", Highest_Cal, "Calories")       
    

elves_file.close()
