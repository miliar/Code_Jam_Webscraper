import sys
import string
import math
def minprod(v1, v2, size):
    if size==1:
        return v1[0]*v2[0]
    if v1[0]<0:
        return v1.pop(0)*v2.pop(size-1)+minprod(v1, v2, size-1)
    else:
        return v1.pop(0)*v2.pop(0)+minprod(v1,v2, size-1)
def compare(x, y):
    if x>=0 and y>=0:
        return cmp(y,x)
    else:
        return cmp(x,y)
        
    
inputfile=open(r'.\input.in', 'r')
outputfile=open(r'.\output.txt','w')
numofcases=string.atoi(inputfile.readline())
for i in range(numofcases):
    size=string.atoi(inputfile.readline())
    v1=map(lambda x: string.atoi(x),inputfile.readline().split())
    v2=map(lambda x: string.atoi(x),inputfile.readline().split())
    v1.sort(compare)
    v2.sort()
    print "Case #%d: %d" % (i+1, minprod(v1, v2, size))
    
