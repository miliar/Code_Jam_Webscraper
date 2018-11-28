#!/usr/bin/env python

import re
import os
import sys
import time
from copy import copy
from itertools import *
import os.path as path

try:
    import psyco
    psyco.full()
except:
    pass

def readint():
    return int(raw_input())

def readfloat():
    return float(raw_input())

def readlinearray(function):
    return map(function, raw_input().split())

def destroy(matrix, x0, y0, M, N, size):
    for y in range(size):
        cy = y + y0
        for x in range(size):
            cx = x + x0
            matrix[cy][cx] = '-20'

def is_chessboard(matrix, x0, y0, M, N, size):
    if y0 + size > M:
        return False
    if x0 + size > N:
        return False
    if size == 1:
        if matrix[y0][x0] in ['0', '1']:
            return True
        return False
    for y in range(size):
        cy = y + y0
        for x in range(size - 1):
            if cy > y0:
                if matrix[cy][x + x0] != matrix[cy - 1][x + x0]:
                    pass
                else:
                    return False
            if int(matrix[cy][x + x0]) + int(matrix[cy][x + x0 + 1]) != 1:
                return False
    destroy(matrix, x0, y0, M, N, size)
    return True

def find_chessboards(matrix, M, N, size, cache = {}):
    if size not in cache:
        cache[size] = []
    for i in range(M):
        for j in range(N):
            if is_chessboard(matrix, j, i, M, N, size):
                cache[size].append((j, i))

def binarize(string): # {{{
    cache = {}
    cache['0'] = '0000'
    cache['1'] = '0001'
    cache['2'] = '0010'
    cache['3'] = '0011'
    cache['4'] = '0100'
    cache['5'] = '0101'
    cache['6'] = '0110'
    cache['7'] = '0111'
    cache['8'] = '1000'
    cache['9'] = '1001'
    cache['A'] = '1010'
    cache['B'] = '1011'
    cache['C'] = '1100'
    cache['D'] = '1101'
    cache['E'] = '1110'
    cache['F'] = '1111'
    s = ''
    for char in string:
        s += cache[char]
    return s
# }}}

def main():
    T = readint()
    for count in range(T):
        print 'Case #' + str(count + 1) + ':',
        cache = {}
        matrix = []
        M, N = readlinearray(int)
        for line in range(M):
            matrix.append(list(binarize(raw_input())))
        for size in range(min(M, N), 0, -1):
            find_chessboards(matrix, M, N, size, cache)
        different = 0
        for l in cache:
            if len(cache[l]) != 0:
                different += 1
        print different
        for l in reversed(cache.keys()):
            if len(cache[l]) != 0:
                print '%d %d' % (l, len(cache[l]))

if __name__ == '__main__':
    main()

