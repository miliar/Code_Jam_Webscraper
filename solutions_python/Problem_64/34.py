import collections
import sys

import numpy

from heapq import heappush, heappop


name = "C-small-attempt1"


class Fakeout(object):
    def __init__(self, stdout, fout):
        self.stdout = stdout
        self.fout = fout

    def write(self, s):
        self.stdout.write(s)
        self.stdout.flush()
        self.fout.write(s)
        self.fout.flush()

sys.stdin = open(name + ".in")
sys.stdout = Fakeout(sys.stdout, open(name + ".out", "w"))


##############

n_cases = input()

for case_number in xrange(1, n_cases + 1):
    m, n = map(int, raw_input().split())
    #*= 4

    board = numpy.array([[-1]*n]*m)

    for row in xrange(m):
        vals = bin(int(raw_input(), 16))[2:]
        vals = "0"*(n-len(vals))+vals
        for col, val in enumerate(map(int, vals)):
            board[row, col] = val

    board[1::2] = 1 - board[1::2]
    board[:,1::2] = 1 - board[:,1::2]

    board = board * 2
    board = 1 - board

    boards = []
    
    for x in xrange(n):
        for y in xrange(m):
            for size in xrange(1, min(n-x+1, m-y+1)):
                if abs(board[y:y+size, x:x+size].sum()) == size * size:
                    heappush(boards, (-size, y, x))
                else:
                    break


    poss = collections.defaultdict(int)
    
    while boards:
        size, y, x = heappop(boards)
        view = board[y:y-size, x:x-size]

        if abs(view.sum()) == size * size:
            poss[-size] += 1
            view[:] = 0

    print "Case #%d:"%case_number, len(poss)
    for k, v in sorted(poss.iteritems(), reverse=True):
        print k, v
