#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Bilal Saim 2017 [Bilisel]
'''
from math import *
import sys
import os
from itertools import *

def algorithm(num,inval):
    ##########################
    #Code Area
    m,n = inval.readline().strip().split()
    m = int(m)
    n = int(n)
    maks = 0
    for i in range(0,n):
        x,y = inval.readline().strip().split()
        x = int(x)
        y = int(y)
        zaman = (m-x)/y
        if zaman > maks:
            maks = zaman



    result = str(m/maks)
    #
    ##########################
    return "Case #"+ str(num+1) +": " + result + "\n"


##########################
#CODES FOR LAZYJAM
##########################
text = ""
data = "test"
infile = "Input-test.txt"
print("Running...")
if os.path.isfile("Operation.txt"):
    with open("Operation.txt","r") as t:
        data = t.readline().strip()
        infile = t.readline().strip()

#We read input values from file
inval = open(infile,"r")

#If there is limit for case!
tnumber = int(inval.readline().strip())
    
for num in range(0,tnumber):
    text += algorithm(num,inval)

dosya = open("Output-"+data+".txt", "w")
dosya.write(text)
dosya.close()

print("Output:")
print(text)

#print(text)
if data == "test":
    with open("Output.txt") as t:
        a = t.readlines()
    with open("Output-test.txt") as t:
        b = t.readlines()

    if a==b:
        print("Results are smiliar")
    else:
        print("Results didn't match!")
