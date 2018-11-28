#!/usr/bin/env python3.2
import sys

def solve(data):
    A = int(data[0])
    B = int(data[1])
    # print("A = %d, B = %d" % (A, B)) # debug
    
    done = set([])
    for n in range(A, B + 1):
        str_n = str(n)
        for i in range(1, len(str_n)):
            m = int(str_n[i:] + str_n[:i])
            # print("n = %d, m = %d" % (n, m)) # debug
            if n < m and A <= m <= B:
                print("Found: n = %d, m = %d" % (n, m))
                done.add((n, m))

    return len(done)

# main
file = "C-sample"
file = "C-small-attempt0"
file = "C-large"

with open(file + ".in", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            data = fdin.readline().split()
            
            result = solve(data)
    
            line = "Case #%d: %d" % (ncase + 1, result)
            print(line) 
            fdout.write("%s\n" % line)