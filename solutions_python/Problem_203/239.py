#!/usr/bin/python3

import sys
import math
from functools import reduce

def solve(R, C, array):

    lst = []

    for r in range(R):
        for c in range(C):
            if array[r][c] != '?':
                lst.append((r, c))

    l = [0] * len(lst)
    r = [0] * len(lst)

    while ''.join([''.join(x) for x in array]).count('?') != 0:
        for (i, (a, b)) in enumerate(lst):
            for k in range(1, 25):
                if b+k < C:
                    if array[a][b+k] == '?':
                        r[i] += 1
                        array[a][b+k] = array[a][b]
                    else:
                        break

        for (i, (a, b)) in enumerate(lst):
            for k in range(1,25):
                if b-k >= 0:
                    if array[a][b-k] == '?':
                        l[i] += 1
                        array[a][b-k] = array[a][b]
                    else:
                        break

        #b 
        for (i, (a, b)) in enumerate(lst):
            for k in range(1, 25):
                if a+k < R:
                    if array[a+k][b] == '?':
                        for ii in range(b-l[i], b+r[i] + 1):
                            array[a+k][ii] = array[a][b]
                    else:
                        break

        for (i, (a, b)) in enumerate(lst):
            for k in range(1, 25):
                if a-k >= 0:
                    if array[a-k][b] == '?':
                        for ii in range(b-l[i], b+r[i] + 1):
                            array[a-k][ii] = array[a][b]
                    else:
                        break



    return array

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        l = get_line()
        R = int(l.split(' ')[0])
        C = int(l.split(' ')[1])
        array = []
        for r in range(R):
            l=get_line()
            array.append(list(l))

        ret = solve(R, C, array)

        print('Case #%d:' %(case_id), file = o)
        for r in ret:
            print(''.join(r))

def get_line():
    return f.readline().strip()

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    (f, o) = open_files()
    main()

