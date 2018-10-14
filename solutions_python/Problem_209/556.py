outp = "Case #{}: {:.7f}"

import math

def totarea(R, H):
    return math.pi * R * R + (2 * math.pi * R) * H

def h_area(R, H):
    return  (2 * math.pi * R) * H
def top_area(R):
    return math.pi * R * R
for T in xrange(int(raw_input())):
    N, K = map(int, raw_input().split())
    pancakes = []
    mta = 0
    mtap = 0
    mtta = 0
    mttap = 0
    mha = 0
    mhap = 0
    for n in xrange(N):
        Ri, Hi = map(int, raw_input().split())
        ta = top_area(Ri)
        tta = totarea(Ri, Hi)
        ha = h_area(Ri, Hi)
        pan = (Ri, Hi, ta, tta, ha)
        if ha > mha:
            mha = ha
            mhap = pan
        if ta > mta:
            mta = ta
            mtap = pan
        if tta > mtta:
            mtta = tta
            mttap = pan
        pancakes.append(pan)
    if K == 1:
        pancakes.sort(key = lambda x: (x[3], x[2], x[0]))
        print outp.format(T+1, pancakes[-1][3])
    else:
        k = K
        pancakes.sort(key = lambda x: (x[4], x[3], x[0]))
        a = sorted(pancakes,key = lambda x: x[4] )
        a.remove(mhap)
        r1 = [mhap] + a[-(k-1):]
        r1.sort(key=lambda x: x[2])
        sr1 = r1.pop(k-1)[3] + sum([x[4] for x in r1])
        b = sorted(pancakes,key = lambda x: x[4] )
        b.remove(mtap)
        r2 = [mtap] + b[-(k-1):]
        r2.sort(key=lambda x: x[2])
        sr2 = r2.pop(k-1)[3] + sum([x[4] for x in r2])
        c = sorted(pancakes,key = lambda x: x[4] )
        c.remove(mttap)
        r3 = [mttap] + c[-(k-1):]
        r3.sort(key=lambda x: x[2])
        sr3 = r3.pop(k-1)[3] + sum([x[4] for x in r3])

        
        print outp.format(T+1, max([sr1, sr2, sr3]))
   
        # print outp.format(T+1, max([sum(sr1), sum(sr2), sum(sr3)]))
    
        
