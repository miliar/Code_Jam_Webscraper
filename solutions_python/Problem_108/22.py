#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
import sys
import math

infinite = 1E+9

class Problem(object):

    def __init__(self):
        pass 

    def sol(self, inp):
        N, vines, L = inp
        vines.sort(key=lambda v: v[0])
        reached = [(0, min(vines[0][0], vines[0][1]))]
        queue = range(1, N)
        while len(reached) > 0:
            i, l = reached.pop(0)
            r = vines[i][0] + l
            if r >= L: return True 
            while len(queue) > 0 and vines[queue[0]][0] <= r:
                next = queue.pop(0)
                d = vines[next][0] - vines[i][0]
                reached.append((next, min(d, vines[next][1])))
        return False

def test_cases(input):
    def intify(l):
        return [int(v) for v in l]

    def floatify(l):
        return [float(v) for v in l]

    fi = open(input, "r")
    T = int(fi.next())
    for i in xrange(1, T + 1):
        N = int(fi.next())
        vines = []
        for j in xrange(N):
            d, l = intify(fi.next().split())
            vines.append((d, l))
        L = int(fi.next())
        yield i, (N, vines, L)
    fi.close()

def main(input, output):
    fo = open(output, "w")
    problem = Problem()
    for i, inp in test_cases(input):
        result = problem.sol(inp)
        fo.write("Case #{0}: {1}\n".format(i, "YES" if result else "NO"))
    fo.close()
        
if __name__ == "__main__":
    # Parse command options
    from optparse import OptionParser
    parser = OptionParser(usage="Usage: %prog [options] param1 param2")    
    parser.add_option("-i", "--input", dest="input", help="Input file")
    parser.add_option("-o", "--output", dest="output", help="Output file")
    options, args = parser.parse_args()
    main(options.input, options.output)
