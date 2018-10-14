# Python 2.7

# This program uses the common NumPy library
# see http://www.numpy.org/

import sys
import numpy


def possible(pattern):
    (rowc, colc) = pattern.shape
    fixed = numpy.array([ [False]*colc ]*rowc, dtype=bool)
    heights = numpy.unique(pattern)

    
    for h in heights[::-1]:     # start with greatest height
        #print("*** {}".format(h))
        #print(fixed)
        for r in range(rowc):
            for c in range(colc):
                if pattern[r, c] == h:
                    if numpy.any(fixed[r]) and numpy.any(fixed[:,c]):
                        #print("Fail at {}, {}".format(r, c))
                        return False
        fixed[pattern == h] = True
    return True



### MAIN ###

f = sys.stdin

count = int(f.readline())

for index in range(1, count+1):
    dim = f.readline().strip()
    dims = dim.split(" ")
    rowc = int(dims[0])
    colc = int(dims[1])
    pattern = numpy.zeros(shape=(rowc, colc), dtype=int)
    
    for r in range(rowc):
        line = f.readline().strip()
        pattern[r] = numpy.fromstring(line, sep=' ', dtype=int)
    
    #print(pattern)
    if possible(pattern):
        yesno = "YES"
    else:
        yesno = "NO"
    
    print("Case #{}: {}".format(index, yesno))