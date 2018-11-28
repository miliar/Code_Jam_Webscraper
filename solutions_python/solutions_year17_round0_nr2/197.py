#!/usr/bin/python3

import sys
import math
from functools import reduce

def solve(l):
    cont = True

    while cont:
        l = [int(i) for i in str(int(l))]
        ll = len(l)
        if ll == 1:
            return l[0]

        cont = False
        for i in range(0, ll-1):
            if l[i] > l[i+1]:
                cont = True
                l[i] = l[i] - 1
                for j in range(i + 1, ll):
                    l[j] = 9

        l = ''.join([str(s) for s in l])

    return l

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        l = get_line()
        ret = solve(l)

        if ret == None:
            l = 'IMPOSSIBLE'
        else:
            l = str(ret)

        print('Case #%d: %s' %(case_id, l), file = o)

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

