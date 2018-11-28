# mpmath library from http://code.google.com/p/mpmath/
from mpmath import *

fin = open('C-small.in', 'r');
fout = open('C-small.out', 'w');

T = int(fin.readline());

mp.dps = 100

for i in range(T):
    fout.write('Case #' + str(i + 1) + ': ')
    n = int(fin.readline())
    N = int((3 + sqrt(5)) ** int(n)) % 1000
    fout.write('%03d' % N)
    fout.write('\n')
    
