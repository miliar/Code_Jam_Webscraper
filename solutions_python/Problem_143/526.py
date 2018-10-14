from Solve import *
from collections import deque

def b(args):
    a, b, k = [int(x) for x in args[0].split(" ")]
    count = 0
    for i in range(0, a):
        for j in range(0, b):
            if (i & j) < k:
                count+=1
    return count

solveF("B-small-attempt0.in", b, 1)
print("done")
#solve("B-large.in", b)
