# template for Google code jam
import sys
import math
import random

def solve(N, wires):
    if N == 1:
        return 0
    total = 0
    for i in range(len(wires)-1):
        for j in range(i+1, len(wires)):
            A1, B1 = wires[i]
            A2, B2 = wires[j]
            if (A1 - A2) * (B1 - B2) < 0:
                total += 1
    return total

def main(filename):
    f = open(filename)
    T = int(f.readline())
    for case in range(1, T+1):
        line = f.readline().strip()
        N = int(line)
        wires = []
        for i in range(N):
            A, B = [int(t) for t in f.readline().split()]
            wires.append((A, B))
        res = solve(N, wires)
        print 'Case #%d:' % case,
        print '%s' % res 
        
    f.close()

if __name__ == '__main__':
    main(sys.argv[1])
    
