#!python
# http://code.google.com/codejam/contest/dashboard?c=1150486#s=p2
from __future__ import division
import math
import sys
from optparse import OptionParser
from collections import deque, defaultdict, OrderedDict
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == "-":
        f = sys.stdin
    else:
        f = open(args[0])
elif not sys.stdin.isatty():
    f = sys.stdin
else:
    parser.error("Need input from file or stdin")

T = int(f.readline())
           
import sieve
import math
import gcd 
       
for i in range(1,T+1):
    N = int(f.readline())
    primes = sieve.sieve(N)
    most = 1 + sum([int(math.floor(math.log(N,p))) for p in primes])
    """if N==1:
        least = 1
    else:
        least = 1   # 1 for N
        lcm = N
        for friend in reversed(range(1,N)):
            if lcm % friend != 0:
                least += 1
                lcm = (lcm * friend) // gcd.gcd(lcm,friend)"""
    guess = max(len(primes),1)
    #print N,most-guess
    #if least != guess:
    #    print N,least,guess
    print "Case #%d: %s" % (i,most-guess)
        
        
