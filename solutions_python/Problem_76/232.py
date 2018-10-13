# -*- coding: utf-8 -*-

import sys
import operator

def calc(items):
    return reduce(lambda x, y: operator.xor(x, y), items)

def solve_case(items):
    items = [int(i) for i in items.split()]
    items.sort()

    min_pile = []
    while items:
        min_pile.append(items.pop(0))
        if items:
            if calc(min_pile) == calc(items):
                return sum(items)
    return None

def test():
    assert solve_case('5 5') == 5
    assert solve_case('5 5 6') is None
    assert solve_case('1 2 3 4 5') is None
    assert solve_case('3 5 6') == 11

if __name__ == '__main__':

    test()

    if len(sys.argv) == 2:
        f = open(sys.argv[1])
        if f:
            f.readline()
            out = open("output.txt", "w")
            idx = 1
            for line in f:
                num = int(line.strip())
                items = f.next().strip()
                r = solve_case(items)
                out.write("Case #%s: %s\n" % (idx, r if r else 'NO'))
                idx += 1
        else:
            print 'Can not open file', sys.argv[1]
    else:
        print 'Invalid parameters number'
