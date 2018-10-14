#!/usr/bin/env python
import numpy as np
from sets import Set

infile = file("in.txt", "r")
outfile = file("out.txt", "w")

#M = 1001
M = 20000001
T = int(infile.readline())

for i in range(1, T+1):
    data = infile.readline().split(" ")
    A = int(data[0])
    B = int(data[1])
    N = len(str(A))
    H = 10**(N-1)
    
    count = 0
    occupied = np.zeros(M, dtype="bool")
    for x in range(A, B+1):
        if occupied[x] == False:
            # permute
            cycles = Set()
            tmp = x
            for j in range(N):
                cycles.add(tmp)
                tmp = tmp%H*10 + tmp/H
            # check unique
            bad = False
            for k in cycles:
                bad = bad or occupied[k]
            # check bad
            backup = cycles.copy()
            for k in  backup:
                if (k < A) or (k > B):
                    cycles.discard(k)
            # count
            if bad == False:
                l = len(cycles)
                count = count + l*(l-1)/2
                for k in cycles:
                    occupied[k] = True
    outfile.write("Case #{}: {}\n".format(i, count))
outfile.close()


