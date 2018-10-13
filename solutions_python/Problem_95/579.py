#from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
import string, re, sys

cipher = 'yhesocvxduiglbkrztnwjpfmaq';
#cipher = "ynficwlbkuomxsevzpdrjgthaq";

def handle(infile, outfile):
    line = infile.readline().split();
    code = [];
    for l in line:
        code.append("".join([cipher[ord(i) - ord("a")] for i in l]));
    outfile.write(' %s' % " ".join(code));

if len(sys.argv) != 2: exit();
infile = file(sys.argv[1] + '.in', 'r');
outfile = file(sys.argv[1] + '.out', 'w');

count = int(infile.readline());
for i in range(count):
    print 'Case #%d' % (i + 1);
    outfile.write('Case #%d:' % (i + 1));
    result = handle(infile, outfile);
    outfile.write('\n');
