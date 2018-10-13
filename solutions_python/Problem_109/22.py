#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
import sys
import math

infinite = 1E+9
def intify(l):
    return [int(v) for v in l]

def floatify(l):
    return [float(v) for v in l]

class Problem(object):

    def __init__(self):
        pass 

    def sol(self, inp):
        N, W, L, R = inp
        index, R = zip(*sorted(enumerate(R), key=lambda t: t[1],
                               reverse=True))
        R = floatify(R)
        i, x = 0, 0
        top, next_top = [(0, -infinite)], []
        result = [None]*N
        for i in xrange(N):            
            if x + R[i] > W:                
                next_top.append((x - R[i], top[0][1]))
                top = next_top
                next_top = []
                x = 0
            y = max(0, top[0][1] + R[i])
            print i
            result[index[i]] = (x, y)
            while len(top) > 1 and x + R[i] >= top[1][0]:
                top.pop(0)
            next_top.append((x - R[i], y + R[i]))
            if i < N - 1:
                x += R[i] + R[i + 1]
            i += 1
        print result
        return result

def test_cases(input):
    fi = open(input, "r")
    T = int(fi.next())
    for i in xrange(1, T + 1):
        N, W, L = intify(fi.next().split())
        R = intify(fi.next().split())
        yield i, (N, W, L, R)
    fi.close()

def main(input, output):
    fo = open(output, "w")
    problem = Problem()
    for i, inp in test_cases(input):
        result = problem.sol(inp)
        fo.write("Case #{0}: ".format(i))
        for x, y in result:
            fo.write("{0} {1} ".format(x, y))
        fo.write("\n")
    fo.close()
        
if __name__ == "__main__":
    # Parse command options
    from optparse import OptionParser
    parser = OptionParser(usage="Usage: %prog [options] param1 param2")    
    parser.add_option("-i", "--input", dest="input", help="Input file")
    parser.add_option("-o", "--output", dest="output", help="Output file")
    options, args = parser.parse_args()
    main(options.input, options.output)
