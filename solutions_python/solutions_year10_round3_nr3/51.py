'''
Created on May 21, 2010

@author: trmcjilt
'''
import sys
from math import sqrt,ceil,floor
filename="C-small-attempt2.in"
#filename="sample.in"
file = open(filename,'r')
sys.stdout = open(filename+".out",'w')


numOfCases = int(file.readline().strip())
caseNum = 1
def subGrid(grid,x,y,size):
#    print len(grid),len(grid[y]),y+size,x+size
    return [grid[z][x:x+size] for z in xrange(y,y+size)]

normGrid = [[True,False]*16,[False,True]*16]*16

    
while numOfCases >= caseNum:
    counter = {}
    M,N = map(int,file.readline().strip().split(' '))
    m = 0
    grid =[]
    while m < M:
        blankRow = [False]*N
        val = [x == '1' for x in bin(int(file.readline().strip(),16))[2:]]
        blankRow[-len(val):] = val
        grid.append(blankRow)
        m+=1
    highest = min(M,N)
    size = highest
    while size > 1:
        mySize = [subGrid(normGrid,0,0,size),subGrid(normGrid,1,0,size)]
        y = 0
        while y+size <= M:
            x = 0
            while x+size <= N and y+size<=M:
                if subGrid(grid,x,y, size)  in mySize:
                    if counter.has_key(size):
                        counter[size]+=1
                    else:
                        counter[size] = 1
                    cleary = y
                    while cleary < y+size:
                        clearx = x
                        while clearx < x+size:
                            grid[cleary][clearx]=size
                            clearx+=1
                        cleary+=1
                    size+=1
                x+=1
            y+=1
        size-=1
    row = 0
#    print grid
    oneDGrid = sum(grid,[])
    my_count = oneDGrid.count(True)+oneDGrid.count(False)
    if my_count:
        counter[1] = my_count 
    value = len(counter)
    print "Case #%(caseNum)s: %(value)s"%locals()
    keys = counter.keys()
    keys.sort()
    keys = reversed(keys)
    for key in keys:
        print "%s %s"%(key,counter[key])
    
#    keys = value.keys()
#    keys.sort
    caseNum+=1
    
    
    
    
    