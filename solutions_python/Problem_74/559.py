from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
import re, sys

def handle(infile, outfile):
    line = infile.readline();
    line = line[:-1].split(' ');
    line = line[1:];
    #print line
    val = [None] * (len(line) / 2);
    for i in range(len(val)):
        val[i] = (line[2 * i], int(line[2 * i + 1]));
    Oi = Bi = cur = time = 0;
    Op = Bp = 1;
    add = False;
    while cur < len(val):
        while Oi < len(val) and val[Oi][0] != 'O':
            Oi += 1;
        if Oi < len(val):
            if Op < val[Oi][1]:
                Op += 1;
            elif Op > val[Oi][1]:
                Op -= 1;
            elif Oi == cur:
                Oi += 1;
                cur += 1;
                add = True;
        while Bi < len(val) and val[Bi][0] != 'B':
            Bi += 1;
        if Bi < len(val):
            if Bp < val[Bi][1]:
                Bp += 1;
            elif Bp > val[Bi][1]:
                Bp -= 1;
            elif Bi == cur and not add:
                Bi += 1;
                cur += 1;
        #print Oi, Bi, cur, Op, Bp;
        add = False;
        time += 1;
    outfile.write(' %d' % time);

if len(sys.argv) != 2: exit()
infile = file(sys.argv[1] + '.in', 'r');
outfile = file(sys.argv[1] + '.out', 'w');

count = int(infile.readline());
for i in range(count):
    print 'Case #%d' % (i + 1);
    outfile.write('Case #%d:' % (i + 1));
    result = handle(infile, outfile);
    outfile.write('\n');
