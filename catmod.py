# -*- coding: utf-8 -*-
"""
catmod for valued pet mobile spa

@author: angel
"""
hours = 0
def weight(lbs):
    lbs = int(input(print("Approximate weight of your cat: "))
    if lbs < 10:
        hours += 1
    elif lbs < 15:
        hours += 2
    else:
        hours += 2.5
    
def coat(hair):
    hair = input(print("Enter 1 for a short-haired cat.\n"
                       "Enter 2 for a long-haired cat.))
    if hair == 1:
        hours += 0
    else:
        hours += 1
                       
    
class Basic:
    "Parent Service"
    
class MedFrou:
    "Parent Service + Half addons"
    
class FrouFrou:
    "Parent Service + Full addons"
    
class Addons:
    "Addons"