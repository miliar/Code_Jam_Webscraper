#!/usr/bin/env python3
from __future__ import division, print_function
import sys
import numpy as np

DATA = u'''3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10'''

def cruise(i, d, h, oh=sys.stdout):
    h = h[h[:,0] < d]
    answer = d/((d - h[:,0])/h[:,1])
    oh.write('Case #{0}:  {1}\n'.format(i+1, answer.min()))

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        from io import StringIO
        fh = StringIO(DATA)
        oh = sys.stdout
    else:
        fh = open(sys.argv[1], 'r')
        oh = open('output.txt', 'w')
    with fh:
        with oh:
            N = int(fh.readline())
            for i in range(N):
                line = fh.readline()
                d, n = [int(_) for _ in line.strip().split()]
                h = []
                for j in range(n):
                    line = fh.readline()
                    h.append([int(_) for _ in line.strip().split()])
                h = np.array(h).astype('float')
                cruise(i, d, h, oh)



