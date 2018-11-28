#! /bin/python
#  LeLouch16 CodeJam '13 Qualification Round

import sys
from math import *
import re

if len(sys.argv) < 3:
    print "Not enough arguments"
    print "Usage '%s input.in output.out'" % sys.argv[0]
    sys.exit()

inpf  = sys.argv[1]
outf  = sys.argv[2]

fin   = sys.stdin if inpf == '-' else open(inpf)
fout  = sys.stdout if outf == '-' else open(outf,'w')

debug = True if '-d' in sys.argv[2:] else False

T = int(fin.readline().strip())
if debug: print "Number of test Cases:",T


#####################

def solve(s,n):
    count = 0
    L     = len(s)
    pat   = ".*[^aeiou]{%d}" % n
    for i in range(L):
        for j in range(i+n,L+1):
            if re.match(pat,s[i:j]):
                count += 1
                if debug: print s[i:j]
    return str(count)

#####################


for i in range(T):
    s,n = fin.readline().strip().split()
    n   = int(n)
    result = solve(s,n)
    s = 'Case #'+str(i+1)+': '+result
    fout.write(s+'\n')
    #if debug: print s



fin.close()
fout.close()

