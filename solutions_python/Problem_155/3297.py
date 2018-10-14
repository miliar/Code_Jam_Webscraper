__author__ = 'Pedro Soriano Casas'

''' Using numpy. http://www.numpy.org/ '''

import numpy as np

if __name__ == '__main__':
    numRange = np.arange(1, 1001)
    aInputFile = open('A-large.in', 'r')
    numberOfTests = int(aInputFile.readline())
    aOutFile = open('A-large.out', 'w')
    for i in xrange(1, numberOfTests + 1):
        (size, theInput) = aInputFile.readline().split(' ')
        f = 0
        if int(size) != 0:
            theNumInput = np.array(','.join(theInput[:-1]).split(','), dtype = int)
            a = theNumInput[0]
            for j, n in enumerate(theNumInput[1:]):
                if n > 0:
                    if (j + 1) > a:
                        f += (j + 1 - a)
                        a = n + j + 1
                    else:
                        a += n

 #           rani = numRange[:int(size)][neededValues[1:]]
 #           theCumSum = theNumInput.cumsum()[:int(size)][neededValues[1:]]
 #           nv = rani - theCumSum
 #           npos = nv[nv>0]
 #           if(len(npos)>0):
 #               n = npos[-1]
        aOutFile.write('Case #%d: %d\n' % (i, f))

