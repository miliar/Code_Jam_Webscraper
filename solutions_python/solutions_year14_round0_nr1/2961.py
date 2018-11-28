# -*- coding: utf-8 -*-

import sys

def solve(data):
    n1 = int(data[0])
    d1 = set(str(data[1: 5][n1 - 1]).split(' '))
    n2 = int(data[5])
    d2 = set(str(data[6:][n2 - 1]).split(' '))

    r = list(d1.intersection(d2))
    l = len(r)
    if l == 1:
        return r[0]
    elif l > 1:
        return "Bad magician!"
    elif l == 0:
        return "Volunteer cheated!"

def process(inp):
    inp = [str(s).strip() for s in inp]
    crt_n = 0
    total_n = int(inp[crt_n])
    crt_n += 1
    for i in range(total_n):
        result = solve(inp[crt_n: crt_n + 10])
        crt_n += 10
        print "Case #%d: %s" % (i + 1, result)

if __name__ == "__main__":
    process(str(sys.stdin.read()).split('\n'))