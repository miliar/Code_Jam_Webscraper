#!/usr/bin/pypy

import sys
from itertools import *

infile = sys.argv[1]
try:
    out = open(sys.argv[2], "w")
except IndexError:
    out = sys.stdout

def read_int(f):
    return int(f.readline())

def read_ints(f, sep=" "):
    return map(int, f.readline().rstrip().split(sep))

def read_lines(f, no_lines):
    retval = []
    for i in xrange(no_lines):
        retval.append(f.readline().rstrip())
    return retval

def solve(max_coins, max_value, denoms, result=0):
#    print max_coins, max_value, denoms, result
    
    if max_coins == 1:
        possible = set()
        len_denoms = len(denoms)
        for config in product([0, 1], repeat=len_denoms):
            s_coins = sum([denoms[i]*config[i] for i in xrange(len_denoms)])
            if s_coins<=max_value and s_coins>0:
                possible.add(s_coins)

            if max_value - len(possible) == 0:
                return result

        missing = set()        
        for i in xrange(1, max_value+1):
            if i not in possible:
                missing.add(i)
                
        print "poss", possible
        print "miss", missing
        

        if len(missing)<=1:
            return len(missing)+result
        
        print "add", min(missing)
        
        return solve(max_coins, max_value, denoms+[min(missing)], result+1)
    else:
        raise ValueError
    
def main():
    f = open(infile, "r")
    no_cases = read_int(f)

    for case_idx in xrange(no_cases):
        max_coins, no_denoms, max_value = read_ints(f)
        denoms = read_ints(f)
        assert len(denoms) == no_denoms
        print "IN max_coins", max_coins, "max_value", max_value, "denoms", denoms
        
        result = solve(max_coins, max_value, denoms)
        
        out.write("Case #%d: %s\n" % (case_idx+1, result))
        
    out.close()
    
if __name__ == "__main__":
    main()
    
    