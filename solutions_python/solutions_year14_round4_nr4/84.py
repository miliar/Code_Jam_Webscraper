import pdb
import sys
import re
import time
from collections import namedtuple
from copy import copy, deepcopy
from pprint import pprint
from glob import glob
import itertools

taskname = 'D'
input = None

def readstr():
    return next(input).strip()

def readintlist():
    lst = map(int, readstr().split())
    return lst

def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]

def node_count(srv):
    return len(set(s[0:idx] for s in srv for idx in xrange(len(s) + 1)))
 
def solvecase():
    string_count, server_count = readintlist()
    strings = [readstr() for _ in xrange(string_count)]
    max_nc, max_ways = 0, 0
    for assignment in itertools.product(*[range(server_count)] * string_count):
        servers = [[] for _ in xrange(server_count)]
        for s, idx in zip(strings, assignment):
            servers[idx].append(s)
        nc = sum(node_count(srv) for srv in servers)
        #print servers, nc
        if nc > max_nc:
            max_nc = nc
            max_ways = 1
        elif nc == max_nc:
            max_ways += 1
    return '{} {}'.format(max_nc, max_ways)

def solve(input_name, output_name):
    global input
    tstart = time.clock()
    input = open(input_name, 'r')
    output = open(output_name, 'w')
    casecount = readint()
    
    for case in range(1, casecount + 1):
        s = solvecase()
        s = "Case #%d: %s" % (case, str(s)) 
        print >>output, s
        print s 
        
    input.close()
    output.close()
    print '%s solved in %.3f' % (input_name, time.clock() - tstart)

def main():
    input_names = glob(taskname + '-*.in')
    assert len(input_names)
    input_names.sort(reverse = True)
    for input_name in input_names:
        solve(input_name, input_name.replace('.in', '.out')) 
                
if __name__ == '__main__':
    main()
