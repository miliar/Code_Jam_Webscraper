from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
import re, sys

def handle(infile, outfile):
    line = infile.readline().split();
    cn = int(line[0]);
    cs = line[1:cn + 1];
    dn = int(line[cn + 1]);
    ds = line[cn + 2:cn + dn + 2];
    s = line[-1];
    #print cs, ds, s
    o = [];
    for i in s:
        if len(o) == 0:
            o.append(i);
            continue;
        x1 = o[-1] + i;
        x2 = i + o[-1];
        done = False;
        for c in cs:
            if x1 == c[:-1] or x2 == c[:-1]:
                o.pop();
                o.append(c[-1]);
                done = True;
                break;
        if done: continue;
        for d in ds:
            if (i == d[0] and d[1] in o) or (i == d[1] and d[0] in o):
                o = [];
                done = True;
                break;
        if done: continue;
        o.append(i);
    o = (', ').join(o);
    outfile.write(' [%s]' % o);

if len(sys.argv) != 2: exit();
infile = file(sys.argv[1] + '.in', 'r');
outfile = file(sys.argv[1] + '.out', 'w');

count = int(infile.readline());
for i in range(count):
    print 'Case #%d' % (i + 1);
    outfile.write('Case #%d:' % (i + 1));
    result = handle(infile, outfile);
    outfile.write('\n');
