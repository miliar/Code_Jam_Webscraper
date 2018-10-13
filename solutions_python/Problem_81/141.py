#!/usr/bin/env python
import sys
import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def rpi(inp):
    ret = []
    for i in inp:
        count = {'.':0, '1':0, '0':0}
        op = []
        for j in range(len(i)):
            count[i[j]] += 1
            if i[j] != '.':
                op.append(j)
        wp = (count['1'], count['1']+count['0'])
        temp = []
        for j in i:
            tw = wp[0] - 1 if j == '1' else wp[0]
            ta = wp[1] if j == '.' else wp[1] - 1
            temp.append(1.0 * tw / ta)
        ret.append([op, wp, temp])
    for i in range(len(ret)):
        owp = 0
        t = 0
        for j in ret[i][0]:
            owp += ret[j][2][i]
            t += 1
        owp /= t
        ret[i].extend([1.0 * ret[i][1][0] / ret[i][1][1], owp])
    for i in range(len(ret)):
        oowp = 0
        t = 0
        for j in ret[i][0]:
            oowp += ret[j][4]
            t += 1
        oowp /= t
        ret[i].append(oowp)
    ret = [(0.25 * i[-3] + 0.50 * i[-2] + 0.25 * i[-1]) for i in ret]
    return ret

case = int(lines[0])
cur = 1
for i in range(1, case + 1):
    l = int(lines[cur])
    inp = []
    for j in range(1, l+1):
        inp.append(list(lines[cur+j][:l]))
    cur += 1 + l
    #print 'Case #%d: %s' % (i, rpi(inp))
    g.write('Case #%d:\n' % i)
    rpis = rpi(inp)
    for j in rpis:
        g.write('%s\n' % str(j))
    #g.write('Case #%d: %s\n' % (i, pos(n, pd, pg)))

g.close()
