import numpy as np
import os
import math

input = open("/ssd/vonna/B-small-attempt1.in",'rb')
output = open("/ssd/vonna/ouput.txt",'wb')

def judge(x):
    x = str(x)
    for id in range(len(x)-1):
        if(x[id+1]<x[id]):
            return True
    return False

def fun(x):
    x = int(x)
    while(judge(x)):
        x -=1
    return x

lines = input.readlines()

for id in range(1,int(lines[0])+1):
    output.write("Case #"+str(id)+": "+str(fun(lines[id]))+"\n")









