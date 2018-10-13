import sys
import math

P = []
maxtime = 0

def split(k):
    res = [[0, k]]
    for i in range(1,min(39, k/2)):
        res.append([i, int(math.ceil(float(k) / float(i+1)))])
    return res

#print split(100)

def calc(stage, shift, time):
    global P, maxtime
    if shift + time >= maxtime:
        return
    if stage >= len(P):
        maxtime = min(maxtime, shift+time)
        return
    el = P[stage]
    var = split(el)
    for v in var:
        calc(stage+1, shift+v[0], max(time, v[1]))

f  = open('/home/alex/workspace/gcj_qual/B-small-attempt0.in')
fo = open('/home/alex/workspace/gcj_qual/bout.txt', 'wb')
T = int(f.readline())
for t in range(T):
    D = int(f.readline().strip())
    P = [int(x) for x in f.readline().strip().split(' ')]
    P = sorted(P, reverse=True)
    maxtime = max(P)
    goodtime = calc(0, 0, 0)
    print "Case #%d: %d" % (t+1, maxtime)
    fo.write("Case #%d: %d\n" % (t+1, maxtime))
fo.close()
f.close()
    