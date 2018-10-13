#!/usr/bin/env python2.5
# encoding: utf-8
import sys
import StringIO
sys.setrecursionlimit(1010)

def numSwitches(engines, queries):
    """ 
    >>> numSwitches(['Yeehaw', 'NSM', 'Dont Ask', 'B9', 'Googol'], \
                    ['Yeehaw', 'Yeehaw', 'Googol', 'B9', 'Googol', 'NSM', 'B9', 'NSM', 'Dont Ask', 'Googol'])
    1
    >>> numSwitches(['Yeehaw', 'NSM', 'Dont Ask', 'B9', 'Googol'], \
                    ['Googol', 'Dont Ask', 'NSM', 'NSM', 'Yeehaw', 'Yeehaw', 'Googol'])
    0
    """
    try:
        return 1 + numSwitches(engines, queries[max(queries.index(e) for e in engines):])
    except ValueError:
        return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    inp = open(sys.argv[1])
    num_cases = int(inp.readline())
    out = open(sys.argv[1].replace(".in", ".out"), "w")
    for case in range(1,num_cases+1):
        num_engines = int(inp.readline())
        engines = [inp.readline().strip() for i in range(num_engines)]
        num_queries = int(inp.readline())
        queries = [inp.readline().strip() for i in range(num_queries)]
        result = "Case #%d: %d" % (case, numSwitches(engines, queries))
        out.write(result + "\n")
