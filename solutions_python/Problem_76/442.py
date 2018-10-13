#!/usr/bin/python
import sys

'''
str1 is a string of integers separated by space
to IntList will return a list of integers 
'''
def toIntList(str1):
    l=str1.split()
    i=0
    while i<len(l):
        l[i]=int(l[i])
        i+=1
    return l

tests = int(sys.stdin.readline())
t=0

while(t<tests):
    n     = sys.stdin.readline()
    nList = toIntList(sys.stdin.readline())

    possible = 0
    sum1 = 0
#    print nList
    min1 = nList[0]
    for x in nList:
        if x < min1:
            min1 = x
        possible ^= x
        sum1 +=x

    answer=""
    if possible != 0:  
        answer = "NO"
    else :
        sum1 -= min1
        answer = str(sum1)
             
    print "Case #"+str(t+1)+": "+answer
    t+=1

