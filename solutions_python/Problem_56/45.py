#!/usr/bin/env python

import re
import sys

class Memoize:
    def __init__(self,function):
        self._cache = {}
        self._callable = function
            
    def __call__(self, *args, **kwds):
        cache = self._cache
        key = self._getKey(*args,**kwds)
        try: return cache[key]
        except KeyError:
            cachedValue = cache[key] = self._callable(*args,**kwds)
            return cachedValue
    
    def _getKey(self,*args,**kwds):
        return kwds and (args, ImmutableDict(kwds)) or args    

def rotated_board(B):
    N = len(B)
    rows = [list() for i in xrange(len(B))]
    for i, row in enumerate(B):
        for j, square in enumerate(row):
            rows[N-1-j].append(square)
    return rows

def apply_gravity(B):
    #import pdb; pdb.set_trace()
    N = len(B)
    rows = [list("."*N) for i in xrange(len(B))]
    for col_n in xrange(N):
        dst_row = N-1
        for src_row in xrange(N-1,-1,-1):
            if B[src_row][col_n] != '.':
                rows[dst_row][col_n] = B[src_row][col_n]
                dst_row = dst_row - 1
    return rows

def show_board(B):
    for row in B:
        print "".join(row)
    print

def has_winner(B, K, c):
    N = len(B)
    for x_delta in (-1,0,1):
        for y_delta in (-1,0,1):
            if x_delta == 0 and y_delta == 0:
                continue
            for x_start in xrange(N):
                x = x_start + x_delta * K
                if x > N or x < 0:
                    continue
                for y_start in xrange(N):
                    y = y_start + y_delta * K
                    if y > N or y < 0:
                        continue
                    for k in xrange(K):
                        if B[x_start+x_delta*k][y_start+y_delta*k] != c:
                            break
                    else:
                        print c, "wins with",K,"in a row"
                        return True
    return False

def test():
    B = [list(x) for x in ("....", "BBBB", "RRRR", "BRBR")]
    has_winner(B, 4, 'B')
    has_winner(B, 4, 'R')

def do_trial(B,K):
    print "-" * 80
    show_board(B)
    print K, "in a row"
    b_wins = False
    r_wins = False
    B = rotated_board(B)
    B = rotated_board(B)
    B = rotated_board(B)
    show_board(B)
    G = apply_gravity(B)
    show_board(G)
    b_wins = b_wins or has_winner(G, K, 'B')
    r_wins = r_wins or has_winner(G, K, 'R')
    if b_wins and r_wins:
        return "Both"
    if b_wins:
        return "Blue"
    if r_wins:
        return "Red"
    return "Neither"

def read_board(f, N):
    B = []
    for i in xrange(N):
        B.append(list(f.readline()[:-1]))
    return B


out = file("out", "w")
f = file("in")

T = int(f.readline()[:-1])
for i in range(T):
    N, K = [int(x) for x in f.readline()[:-1].split()]
    B = read_board(f, N)
    v = do_trial(B,K)
    print "Case #%d: %s" % (i+1, v)
    print >>out, "Case #%d: %s" % (i+1, v)
    out.flush()
