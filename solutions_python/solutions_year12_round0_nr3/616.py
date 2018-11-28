#!/opt/local/bin/python3.2
import sys
import time
def rotations(x):
    for (i,c) in enumerate(x):
        if c<x[0]: continue 
        yield x[i:]+x[:i]

def rotbetween(i,a,b):
    return len(set(x for x in rotations(i) if i<x and a<=x<=b))
def solve(a,b):
    s=0
    for i in range(int(a),int(b)+1):
        s+=rotbetween(str(i),a,b)
    return s
for (i,s) in enumerate(sys.stdin.readlines()):
    if i==0: continue
    (a,b)=s.strip().split(' ')
    assert len(a)==len(b)
#    start = time.time()
    print('Case #{0}: {1}'.format(i,solve(a,b)))
#    print(time.time() - start)
