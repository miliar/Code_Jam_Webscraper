'''
Created on 12 Apr 2014

@author: franovic
'''
def play_war(N,p1,p2):
    p1.sort()
    p2.sort(reverse=True)
    answer=0
    for i in xrange(N):
        s1=p1.pop()
        for s in p2:
            if s>s1:
                p2.remove(s)
                break
        else:
            p2.pop()
            answer+=1
    return(answer)
def play_dwar(N,p1,p2):
    p1.sort(reverse=True)
    p2.sort()
    answer=0
    for i in xrange(N):
        if p1[0]<p2[-1]:
            p1.pop()
            p2.pop()
        else:
            p1=p1[1:]
            p2.pop()
            answer+=1
    return(answer)
import sys
fn_in = sys.argv[1]
fn_out = '.'.join(fn_in.split('.')[:-1]+ ['out'])
f1 = open(fn_in, 'r')
out=''
T=int(f1.readline().rstrip())
for t in xrange(1,T+1):
    N = int(f1.readline().rstrip())
    p1 = [float(x) for x in f1.readline().rstrip().split()]
    p2 = [float(x) for x in f1.readline().rstrip().split()]
    out += 'Case #%d: %d %d\n' % (t, play_dwar(N,p1[:],p2[:]),play_war(N,p1[:],p2[:]))
f1.close()
f2 = open(fn_out, 'w+')
f2.write(out.rstrip())
f2.close()