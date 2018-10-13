'''
Created on 12 Apr 2014

@author: franovic
'''
import sys
fn_in = sys.argv[1]
fn_out = '.'.join(fn_in.split('.')[:-1]+ ['out'])
f1 = open(fn_in, 'r')
out=''
T=int(f1.readline().rstrip())
for t in xrange(1,T+1):
    [C, F, X] = [float(x) for x in f1.readline().rstrip().split()]
    maxF = int(X/C)
    answer = X/2.0;
    ttbf=0
    for i in xrange(maxF+1):
        ttotal = ttbf+X/(2.0+i*F)
        if ttotal<answer:
            answer = ttotal
        ttbf+=C/(F*i+2.0)
    out += 'Case #%d: %.7f\n' % (t, answer)
f1.close()
f2 = open(fn_out, 'w+')
f2.write(out.rstrip())
f2.close()