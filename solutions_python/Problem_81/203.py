from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
import re, sys

def handle(infile, outfile):
    line = infile.readline().split();
    n = int(line[0]);
    wm = [None] * n;
    lm = [None] * n;
    w = [0] * n;
    l = [0] * n;
    for i in range(n):
        wm[i] = [0] * n;
        lm[i] = [0] * n;
        line = infile.readline()[:-1];
        for j in range(n):
            if line[j] == '0':
                l[i] += 1;
                lm[i][j] = 1;
            elif line[j] == '1':
                w[i] += 1;
                wm[i][j] = 1;
    
    wp = [None] * n;
    for i in range(n):
        wp[i] = [0] * n;
        for j in range(n):
            wp[i][j] = (w[i] - wm[i][j]) * 1.0 / (w[i] + l[i] - wm[i][j] - lm[i][j]);
    
    rpi = [0] * n;
    for i in range(n):
        rpi[i] = 0.25 * w[i] / (w[i] + l[i]);
        avgwp = 0;
        c = 0;
        for j in range(n):
            if wm[i][j] or lm[i][j]:
                avgwp += wp[j][i];
                c += 1;
        rpi[i] += 0.5 * avgwp / c;
        avgowp = 0;
        d = 0;
        for j in range(n):
            if wm[i][j] or lm[i][j]:
                avgtemp = 0;
                c = 0;
                d += 1;
                for k in range(n):
                    if wm[j][k] or lm[j][k]:
                        avgtemp += wp[k][j];
                        c += 1;
                avgowp += avgtemp / c;
        rpi[i] += 0.25 * avgowp / d;
    for i in range(n):
        outfile.write('\n%.10f' % rpi[i]);

if len(sys.argv) != 2: exit();
infile = file(sys.argv[1] + '.in', 'r');
outfile = file(sys.argv[1] + '.out', 'w');

count = int(infile.readline());
for i in range(count):
    print 'Case #%d' % (i + 1);
    outfile.write('Case #%d:' % (i + 1));
    result = handle(infile, outfile);
    outfile.write('\n');
