#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')

from collections import defaultdict

def run():
    Ac, Aj = map(int,input.readline().split())
    T = []
    for i in range(Ac):
        x, y = map(int,input.readline().split())
        T.append((0,x,y))
    for i in range(Aj):
        x, y = map(int,input.readline().split())
        T.append((1,x,y))

    T.sort(key=lambda((a,x,y)): x)
    
    A0 = sum([y-x for (a,x,y) in T if a==0])
    A1 = sum([y-x for (a,x,y) in T if a==1])
    assert A0 <= 720
    assert A1 <= 720

    TT = T + [(T[0][0], T[0][1]+720*2, T[0][2]+720*2)]
    
    count = 0
    total_change = 0
    other = []
    print "TT=", TT
    for i in range(len(T)):
        t=TT[i+1][1] - TT[i][2]
        if TT[i][0] != TT[i+1][0]:
            count += 1
            total_change += t
        else:
            other.append(t)
    other.sort()
    print "changes/minutes: ", count, total_change
    print "other: ", other
    assert count % 2 == 0
    z = min(A0,A1) + total_change
    assert A0 + A1 + total_change + sum(other) == 720*2
    while z < 720:
        count += 2
        z += other.pop()
    return count
    
    
T = int(input.readline())
for t in range(T):
    print >> output, 'Case #{}: {}'.format(t+1,run())
