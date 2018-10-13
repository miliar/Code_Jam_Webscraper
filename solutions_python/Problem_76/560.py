from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
import re, sys

def xor(l):
    return reduce(lambda x, y: x ^ y, l, 0);

def score(l1, l2, x1, x2, s1, s2, skip):
    #print l1, l2;
    #raw_input();
    if s2 > s1:
        return -1;
    if len(l2) > 0 and x1 == x2:
        return s1;
    for i in range(len(l1) - skip):
        n = l1.pop(i);
        l2.append(n);
        v = score(l1, l2, x1 ^ n, x2 ^ n, s1 - n, s2 + n, i + skip);
        if v > -1:
            return v;
        else:
            n = l2.pop();
            l1.append(n);
    return -1;

def handle(infile, outfile):
    line = infile.readline();
    l = sorted([int(x) for x in infile.readline().split()]);
    x1 = xor(l);
    x2 = 0;
    s1 = sum(l);
    s2 = 0;
    s = score(l, [], x1, x2, s1, s2, 0);
    if s == -1:
        s = 'NO';
    else:
        s = str(s);
    outfile.write(' %s' % s);

if len(sys.argv) != 2: exit();
infile = file(sys.argv[1] + '.in', 'r');
outfile = file(sys.argv[1] + '.out', 'w');

count = int(infile.readline());
for i in range(count):
    print 'Case #%d' % (i + 1);
    outfile.write('Case #%d:' % (i + 1));
    result = handle(infile, outfile);
    outfile.write('\n');
