from library import *

f = file('a.in1','r')
T = readint(f)
for case in range(1,T+1):
    R1 = readint(f)
    for i in range(4):
        if i == R1-1:
            D1 = set(readints(f))
        else: f.readline()
    R2 = readint(f)
    for i in range(4):
        if i == R2-1:
            D2 = set(readints(f))
        else: f.readline()
    S = D1 & D2
    if len(S) == 0:
        print 'Case #%d: Volunteer cheated!' % case
    if len(S) > 1:
        print 'Case #%d: Bad magician!' % case
    if len(S) == 1:
        print 'Case #%d: %d' % (case, S.pop())
