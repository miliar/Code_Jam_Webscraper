#from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
from collections import deque
import re, sys

def handle(infile, outfile):
    line = infile.readline().split();
    a = int(line[0]);
    b = int(line[1]);
    v = 0;
    d = len(str(a));
    ten2d = 10 ** (d - 1);
    bag = set();
    for n in range(a, b + 1):
        m = n;
        for i in range(d - 1):
            m = (m % 10) * ten2d + m / 10; # rotate
            if m >= a and m <= b and m != n:
                bag.add(m);
        v = v + len(bag);
        bag.clear();
    outfile.write(' %d' % (v / 2));

if len(sys.argv) != 2: exit();
infile = file(sys.argv[1] + '.in', 'r');
outfile = file(sys.argv[1] + '.out', 'w');

count = int(infile.readline());
for i in range(count):
    print 'Case #%d' % (i + 1);
    outfile.write('Case #%d:' % (i + 1));
    result = handle(infile, outfile);
    outfile.write('\n');
