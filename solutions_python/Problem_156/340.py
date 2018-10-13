from collections import *
from copy import *
from math import *

def choice(index,pancakes,strategy):
    if index==len(pancakes):
        return max([ceil(float(pancakes[i])/strategy[i]) for i in range(len(pancakes))])
    minTime = float('infinity')
    for i in range(pancakes[index]+1):
        strategy[index]=i+1
        t = i+choice(index+1,pancakes,strategy)
        #print choice(index+1,pancakes,strategy),t
        if t<minTime:
            minTime = t
    return minTime
    
if __name__=='__main__':
    input=open('B-small.in.txt','r+')
    output=open('B-small.out.txt','w+')

    numCases = int(input.readline().strip())
    for case in range(1,numCases+1):
        numDiners = int(input.readline().strip())
        pancakes = []
        line = input.readline().strip().split()

        strategy = []
        for i in range(numDiners):
            pancakes.append(int(line[i]))
            strategy.append(1)

        time= choice(0,pancakes,strategy)
        
        output.write("Case #%d: %d\n"%(case,time))
        

    input.close()
    output.close()