#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Bilal Saim 2017 [Bilisel]
'''
import math
import sys
import os

def algorithm(num,inval):
    ##########################
    #Code Area
    d,n = inval.readline().strip().split()
    n = int(n)
    say = 0
    for i in range(len(d)-1,-1,-1):
        var = True
        if d[i] == "-":
            if i<(n-1):
                var = False
                
                break
            say += 1
            for j in range(i,i-n,-1):
                if d[j] == "+":
                    d = d[:j] + "-" + d[j + 1:]
                else:
                    d = d[:j] + "+" + d[j + 1:]
    if not var:
        result = "IMPOSSIBLE"
    else:
        result = str(say)

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
