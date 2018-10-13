##            Google Code Jam 2008
##            Round 1C
##            Task: A
##            Language: Python
##            Input: standard input
##            Output: standard output

from math import *
from re import *
from sys import *

def read_numbers(filename=stdin):
    temp=filename.readline().strip().split();
    result=[];
    for x in temp:
        result.append(int(x))
    return result

## Main program  
solution=""
total_case=int(stdin.readline())
## Loop of the cases
for case in range(1,total_case+1):
## Init
    OK=0
    input=read_numbers()
    freq=read_numbers()
    
    max_let=input[0]
    keys=input[1]
    letters=input[0]            
##  Solving the problem    
    freq.sort()
    freq.reverse()
    counter=0;
    press=1
    total=0
    for i in range(0,len(freq)):
        counter+=1
        if counter>keys:
            press+=1
            counter=1
        total=total+freq[i]*press
        
## Solution
    print "Case #%i: %s" % (case,total)
