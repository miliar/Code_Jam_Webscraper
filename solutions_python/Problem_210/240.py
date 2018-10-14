from __future__ import division
lines = open('B-small-attempt2.in').read().splitlines()
# lines = open('input.txt').read().splitlines()
pos = 0
import math
pi = math.pi
# Don't forget to do pos+1 after using these.
r_i = lambda: int(lines[pos].strip())
r_is = lambda: map(int, lines[pos].strip().split())
r_s = lambda: lines[pos].strip()
r_ss = lambda: lines[pos].strip().split()
r_f = lambda: float(lines[pos].strip())
r_fs = lambda: map(float, lines[pos].strip().split())

test = r_i()
pos+=1
out = open('output3.txt', 'w')

ans = 0
for t in range(test):
    ac, aj = r_is()
    pos+=1
    cam = []
    act, ajt = [], []
    for i in range(ac):
        c, d = r_is()
        pos+=1
        act.append((c, d))
    for i in range(aj):
        c,d = r_is()
        pos+=1
        ajt.append((c,d))
    if ac==0 and aj==1:
        ans = 2
    elif aj==0 and ac==1:
        ans = 2
    elif ac==1 and aj==1:
        ans = 2
    elif ac==0 and aj==2:
        maxs = max(ajt[0][1], ajt[1][1])
        maxs2 = min(ajt[0][1], ajt[1][1])
        minf = min(ajt[0][0], ajt[1][0])
        minf2 = max(ajt[0][0], ajt[1][0])
        temp = min(maxs-minf, 24*60 - (minf2-maxs2))
        if temp <= 12*60:
            ans = 2
        else:
            # print ajt
            ans = 4
    elif ac==2 and aj==0:
        maxs = max(act[0][1], act[1][1])
        maxs2 = min(act[0][1], act[1][1])
        minf = min(act[0][0], act[1][0])
        minf2 = max(act[0][0], act[1][0])
        temp = min(maxs-minf, 24*60 - (minf2-maxs2))
        # print maxs, minf, minf2, maxs2
        if temp <= 12*60:
            ans = 2
        else:
            # print act
            ans = 4
    else:
        print "case %d ------------------ " %(t+1)


    # Result contains answer
    # print ac,aj
    # print act, ajt
    temp = "Case #%d: %d" % (t+1, ans)
    print temp
    out.write(temp+'\n')

out.close()
