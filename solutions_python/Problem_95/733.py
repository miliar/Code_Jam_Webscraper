import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'A'
input = None

sample_input = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
y qee
'''
sample_output = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
a zoo
'''

a_z = set(chr(c) for c in xrange(ord('a'), ord('z') + 1)) 

def filter_letters(s):
    res = []
    for c in s:
        if c in a_z:
            res.append(c)
    return ''.join(res)

def make_trans_table():
    t = {}
    src, dst = filter_letters(sample_input), filter_letters(sample_output)
    assert len(src) == len(dst)
    for s, d in zip(src, dst):
        if s not in t:
            t[s] = d
        else:
            assert t[s] == d
    assert len(t) == 25
    s_set = set(t.keys())
    d_set = set(t.values())
    s_missing = a_z - s_set
    d_missing = a_z - d_set
    assert len(s_missing) == 1 and len(d_missing) == 1
    t[s_missing.pop()] = d_missing.pop()    
    return t


def readstr():
    return next(input).strip()

def readintlist():
    lst = map(int, readstr().split())
    return lst

def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]

def solvecase():
    s = readstr()
    r = []
    for c in s:
        if c in trans_table:
            r.append(trans_table[c])
        else:
            assert c == ' '
            r.append(c)
    return ''.join(r)

def solve(suffix):
    global input
    tstart = time.clock()
    input = open(taskname + '-' + suffix + '.in', 'r')
    output = open(taskname + '-' + suffix + '.out', 'w')
    casecount = readint()
    
    for case in range(1, casecount + 1):
        s = solvecase()
        s = "Case #%d: %s" % (case, str(s)) 
        print >>output, s
        print s 
        
    input.close()
    output.close()
    print '%s solved in %.3f' % (suffix, time.clock() - tstart)
            
if __name__ == '__main__':
    trans_table = make_trans_table()
    print trans_table
    print len(trans_table)
    solve('small')
    solve('large')
