from io import *
from math import *
from decimal import *

def runFile(file):
    f = open(file)
    g = open("output" + file, 'w')
    num = int(f.readline().rstrip('\n'))
    for i in range(num):
        [a,n] = f.readline().strip("/n").split(' ')
        moteSize = f.readline().strip("\n").split(' ')
        moteSize = [int(i) for i in moteSize]
        moteSize.sort()
        ans = mReduce(moteSize,0,int(a))
        print(ans)
        g.write("Case #" + str(i+1) + ": " + str(ans) + "\n")

def mReduce(moteSize,count,size):
    if(size == 1):
        return len(moteSize)
    if(len(moteSize) == 1):
        if(moteSize[0] >= size):
            return count+1
        else:
            return count
    else:
        if(moteSize[0] >= size):
            return min(mReduce(moteSize,count+1,2*size-1),mReduce(moteSize[1:],count+1,size))
        else:
            return mReduce(moteSize[1:],count,size+moteSize[0])
