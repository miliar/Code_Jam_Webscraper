# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 01:02:47 2017

@author: Oliver
"""

inputfile = open("D:/EhemalsDesktop/Rest/Courses/Google Code Jam/2017/B-small-attempt0.in","r")
outputfile = open("D:/EhemalsDesktop/Rest/Courses/Google Code Jam/2017/Bsmall.txt","w+")
num_of_testcases = int(inputfile.readline())
inputs = []
for i in range(1,num_of_testcases+1):
    inputs.append(int(inputfile.readline()))

def testTidy(number):
    strNum = str(number)
    L = []
    tidy = True
    for integer in strNum:
        L.append(integer)
    for index in range(len(L)-1):
        if L[index] <= L[index+1]:
            next
        else:
            tidy = False
    return tidy

def genNumbers(inputs):
    outputs =[]
    for number in inputs:
        holdNumber = number
        if testTidy(holdNumber) == True:
            outputs.append(holdNumber)
        else:
            tidy = testTidy(holdNumber)
            while tidy==False:
                holdNumber -= 1
                tidy = testTidy(holdNumber)
            outputs.append(holdNumber)
    return outputs
    
output = genNumbers(inputs)
count = 0

for number in output:
    count +=1
    outputfile.write("Case #" + repr(count) + ": " + repr(number) +"\n")
    
inputfile.close()
outputfile.close()