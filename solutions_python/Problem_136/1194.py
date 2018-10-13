import os
import re
import math
from collections import deque
import heapq
import time


def get_time(c, f, x):
    t = 0
    k = int(math.ceil((x * f - 2 * c) / (c * f) - 1))
    if k > 0:
        for i in range(0, k):
            dt = c / (i * f + 2)
            if dt * (k-i) < 0.0000001:
                break
            t += dt
        t += x / (k * f + 2)
    else:
        t = x / 2
    return t

def main(fin, fout):
    start = time.clock()
    fin = open(fin, 'r')
    fout = open(fout, 'w')
    k = int(fin.readline())
    for i in range(k):
        c, f, x = [float(w) for w in fin.readline().split()]
        t = get_time(c, f, x)
        fout.write('Case #' + str(i + 1) + ': ')
        fout.write('%.7f' % t)
        fout.write('\n')
        if i % 10 == 9:
            print 'Case #' + str(i + 1) + '/' + str(k) + ' ' + 'finished, %.3f' % (time.clock() - start) + ' sec taken'
    fin.close()
    fout.close()
    pass

if __name__ == '__main__':
    problem = 'B'
    _fin = problem + '/B-large.in'
    _fout = _fin[:-2] + 'out'
    main(_fin, _fout)
