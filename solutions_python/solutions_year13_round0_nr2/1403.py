#!/usr/bin/env python

inputs = 'B-large.in'

f = open(inputs, 'r')

numline = 1
lineN   = 0
N       = 0
M       = 0
l       = []
case    = 0
out     = ''

def rec_list(mlist, fg = True):
    if len(mlist) == 0:
        return 'YES'
    elif fg == False:
        return 'NO'
    else:
        indr = 0
        indc = 0
        tmpr = 0
        tmpc = 0
        mmin = 100
        M = len(mlist[0])
        N = len(mlist)

        for i in xrange(0, N):
            if mmin > min(mlist[i]):
                mmin = min(mlist[i])
                indr = i
                indc = mlist[i].index(min(mlist[i]))
        
        # cek row
        for i in xrange(0,M):
            if mlist[indr][i] == mmin:
                tmpr += 1

        # cek column
        for i in xrange(0,N):
            if mlist[i][indc] == mmin:
                tmpc += 1

        flagdel = False

        if tmpr == M:
            flagdel = True
            del mlist[indr]

        elif tmpc == N:
            flagdel = True
            for i in xrange(0,N):
                del mlist[i][indc]

        if len(mlist):
            size2 = len(mlist[0]) * len(mlist)
        return rec_list(mlist, flagdel)

for line in f:
    v = line.strip()

    if numline == 1:
        numline += 1
        continue

    if N == 0 or (numline > (N + lineN)):
        if N > 0:
            case += 1
            size = M*N
            xx = rec_list(l)
            out += 'Case #%i: %s\n' % (case, xx)
            l = []

        lineN = numline
        N = int(v.split(' ')[0])
        M = int(v.split(' ')[1])
        numline += 1
        continue
    else:
        l.append(map(int, v.split(' ')))
    
    numline += 1

f.close()

case += 1
size = M*N
xx = rec_list(l)
out += 'Case #%i: %s\n' % (case, xx)

with open ('outbig', 'w') as f: 
    f.write (out)