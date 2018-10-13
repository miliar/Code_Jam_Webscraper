from __future__ import print_function
import sys
import numpy as np

def getflips(status, flipsize):
    numflips = 0
    for i in range(0,len(status)-(flipsize-1)):
        if status[i] == -1:
            status[i:i+flipsize] = status[i:i+flipsize] * -1
            numflips += 1
    for i in status[-(flipsize-1):]:
        if i == -1:
            return 'IMPOSSIBLE'
    return str(numflips)

#Read data
probset = []
with open(sys.argv[1], "r") as f:
    T = int(f.readline())
    for x in range(T):
        flipstatus, flippersize = f.readline().split()
        flippersize = int(flippersize)
        flipstatus = np.array([1 if x == '+' else -1 for x in list(flipstatus)])
        roads = {}
        probset.append([flipstatus, flippersize])
x = 1
for prob in probset:
    print("Case #%d: %s" % (x, getflips(prob[0], prob[1])))
    x += 1
    


# In[ ]:



