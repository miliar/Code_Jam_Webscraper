import os
import re
import math
from collections import deque
import heapq
import time


def function(A, B, K):
    cnt = 0
    for a in range(0, A):
        for b in range(0, B):
            if a & b < K:
                cnt += 1
    return cnt


def main(fin, fout):
    start = time.clock()
    fin = open(fin, 'r')
    fout = open(fout, 'w')
    k = int(fin.readline())
    for i in range(k):
        A, B, K = [int(w) for w in fin.readline().split()]

        R = function(A, B, K)

        fout.write('Case #' + str(i + 1) + ': ')

        fout.write(str(R) + '\n')
        print('Case #' + str(i + 1) + ': ' + str(R))

        #output

        if i % 10 == 9:
            print('Case #' + str(i + 1) + '/' + str(k) + ' ' + 'finished, %.3f' % (time.clock() - start) + ' sec taken')
    fin.close()
    fout.close()
    pass

if __name__ == '__main__':
    problem = 'B'
    _fin = problem + '/B-small-attempt0.in'
    _fout = _fin[:-2] + 'out'
    main(_fin, _fout)

