'''
Created on Oct 19, 2009

@author: sg0892495
'''
import string

dynamicMap={}

def converse():
    file.readline()
    numbers=file.readline().split()
    numbers=map(int,numbers)
    numbers.sort()
    xorVal=0
    for num in numbers:
        xorVal = xorVal ^ num
    if(xorVal!=0):
        return "NO"
    else:
        return sum(numbers[1:])
    
    
    

                 

file = open('./a2.in')
for i in range(0,string._int(file.readline())):
    print 'Case #%s: %s' %((i+1), converse())

