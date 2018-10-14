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
    a1 = int(f1.readline().rstrip())
    l1 = []
    for i in xrange(4):
        ll = f1.readline().rstrip().split()
        if i+1==a1:
            for l in ll:
                l1.append(int(l))
    a2 = int(f1.readline().rstrip())
    ret = []
    for i in xrange(4):
        ll = f1.readline().rstrip().split()
        if i+1==a2:
            for l in ll:
                if int(l) in l1:
                    ret.append(int(l))
    if len(ret)==1:
        answer = ret[0]
    elif len(ret)==0:
        answer = "Volunteer cheated!"
    else:
        answer = "Bad magician!"
    out += 'Case #%d: %s\n' % (t, answer)
f1.close()
f2 = open(fn_out, 'w+')
f2.write(out.rstrip())
f2.close()