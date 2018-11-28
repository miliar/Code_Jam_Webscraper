import sys
import math
import numpy as np
from pprint import pprint

numTests = int(sys.stdin.readline().rstrip("\n"))

def solve(rows,cols,width):
    if( cols == width):
        return rows + (width -1)
    elif( width == 1):
        return rows*cols
    else:
        v = (cols +1 -width)
        if( v % width == 0):
            return (v/width) - 1 + width + 1
        elif ( v%width == 1):
            return (v/width) + width
        else:
            # return (v/width) + (v%width)-1 + width
            return (v/width) + width + 1

        # return (cols + 1 -width)/width + width
        # return rows*((cols - width) - (width - 1) + 1 + (width -1))

for test_num in xrange(numTests):
    Rows,Cols,W  = map(int,sys.stdin.readline().rstrip("\n").split(" "))
    answer = solve(Rows,Cols,W)
    print("Case #"+ str(test_num + 1) + ": " + str(answer))
    # print("Case #"+ str(test_num + 1) + ": " + str(answer) +" " + str(Rows) + " "  + str(Cols) + " " + str(W))
