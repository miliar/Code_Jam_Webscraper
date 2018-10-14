from math import *

f = open('A-large (1).in', 'r')
fout = open('Download A-small.out', 'w')
T=int(f.readline())
for i in xrange(0, T):
    string = f.readline()
    N, K = str.split(string,' ', 1)
    if (long(K)+1)%pow(2, long(N)) == 0:
        print 'ON'
        value = 'Case #'+ str(i+1)+ ': ON\n'
        
    else:
        print 'OFF'
        value = 'Case #'+ str(i+1)+ ': OFF\n'
    fout.write(value)
f.close()
fout.close()
