#!/usr/bin/python

import sys
import numpy

def cutLawn(rows,cols,matrixResult,rowHeights,colHeights):
    for i in range(rows):
        for j in range(cols):
            if matrixResult[i,j] not in [rowHeights[i],colHeights[j]]:
                return False
    return True

    
if len(sys.argv)>=2:
    fileIn = sys.argv[1]
else:
    fileIn = 'example.txt'


with open(fileIn) as f:
    for case in range(int(f.readline())):
        (rows, cols) = f.readline().strip().split(' ')
        (rows, cols) = (int(rows), int(cols))
        m = list()
        maxCol = [None]*cols
        maxRow = [None]*rows
        for i in range(rows):
            m.append(f.readline().strip().split(' '))
            maxRow[i] = max(m[i])
        m = numpy.matrix(m).T.tolist()
        for i in range(cols):
            maxCol[i] = max(m[i])
        m = numpy.matrix(m).T
        if cutLawn(rows,cols,m,maxRow,maxCol):
            print "Case #%d: YES" % (case+1)
        else:
            print "Case #%d: NO" % (case+1)

            
        
