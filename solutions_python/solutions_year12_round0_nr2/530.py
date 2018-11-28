#from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
import re, sys

def handle(infile, outfile):
    line = infile.readline().split();
    n = int(line[0]);
    s = int(line[1]);
    p = int(line[2]);
    t = sorted([int(i) for i in line[3:]], reverse=True);
    v = 0;
    for i in t:
        x = i / 3;
        y = i % 3;
        if x >= p:
            v = v + 1;
        elif y > 0 and x + 1 >= p:
            v = v + 1;
        elif s > 0:
            if x > 0 and x + 1 >= p:
                v = v + 1;
                s = s - 1;
            elif y == 2 and x + 2 >= p:
                v = v + 1;
                s = s - 1;
    # t / 3 = x.00 -> x x x or x-1 x x+1
    # t / 3 = x.33 -> x x x+1 or x-1 x+1 x+1
    # t / 3 = x.66 -> x x+1 x+1 or x x x+2
    outfile.write(' %d' % v);

if len(sys.argv) != 2: exit();
infile = file(sys.argv[1] + '.in', 'r');
outfile = file(sys.argv[1] + '.out', 'w');

count = int(infile.readline());
for i in range(count):
    print 'Case #%d' % (i + 1);
    outfile.write('Case #%d:' % (i + 1));
    result = handle(infile, outfile);
    outfile.write('\n');
