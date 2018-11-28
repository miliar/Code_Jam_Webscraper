'''
Created on 14-Apr-2012

@author: abhijit
'''
import math
def calculate_recycle(num):
    val=0
    while(len(num)!=0):
        #print num
        cycles=get_cycle(num[0])
       
        for cycle in cycles:
            if(num.__contains__(cycle)):
                #print str(num[0])+" "+str(cycle)
                val+=1
        
        num.remove(num[0])
    return val

def get_cycle(no):
    cycles=[]
    ns=str(no)
    le=len(ns)
    for i in range(1,le):
        x=ns[:i]
        y=ns[(i):le]
        
        z=y+x
        
        re=int(z)
        if(len(str(re))==le and re!=no):
            cycles.append(re)
    cycles=set(cycles)
    cycles=list(cycles)
    cycles.sort()
    
    return cycles         

input_val=int(raw_input())
strings=[]

numbers=[]
for i in range(input_val):
    string=raw_input()
    strings.append(string)

case=1
for string in strings:
    params=string.split()
    A=int(params[0])
    B=int(params[1])
    
    for i in range(A,B+1):
        numbers.append(i)
    val=calculate_recycle(numbers)
    print "Case #"+str(case)+": "+str(val)
    case+=1