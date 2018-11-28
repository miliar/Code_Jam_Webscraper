__author__ = 'Victor Villar'

from numpy import array
from math import ceil

def computeTimeAtStep(n, x, c, f, f0 = 2.):
    f = float(f)
    c = float(c)
    x = float(x)
    f0 = float(f0)
    timesF = array([1/(f0 + i*f) for i in range(n)])
    totalFarmTime = c * timesF.sum()
    totalXTime = x / (f0 + n*f)
    return totalFarmTime + totalXTime

def getOptimalStep(x, c, f, f0 = 2.):
    f = float(f)
    c = float(c)
    x = float(x)
    f0 = float(f0)
    nFloat = x/c - f0/f - 1
    return max(0,int(ceil(nFloat)))

if __name__ == '__main__':
    inFile = open('B-large.in','r')
    numberOfTests = int(inFile.readline())
    outFile = open('B-large.out','w')
    for i in range(1, numberOfTests + 1):
        (C, F, X) = inFile.readline().split()
        step = getOptimalStep(X, C, F)
        answer = computeTimeAtStep(step, X, C, F)
        outFile.write('Case #%d: %.7f\n' % (i, answer))