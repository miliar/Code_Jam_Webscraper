'''
Created on Oct 19, 2009

@author: sg0892495
'''
import string

dynamicMap={}

def converse():
    numbers=map(int,file.readline().split())
    players=map(int,file.readline().split())
    for i in range(numbers[1],numbers[2]+1):
        found=True
        for player in players:
            if((i % player != 0) and (player % i != 0)):
                found=False
                break
        if(found):
            return i
    return "NO"
    
    
    

                 

file = open('./b1.in')
for i in range(0,string._int(file.readline())):
    print 'Case #%s: %s' %((i+1), converse())

