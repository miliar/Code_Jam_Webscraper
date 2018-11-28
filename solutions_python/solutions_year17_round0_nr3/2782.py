# your code goes here
from sys import stdin

t = int(stdin.readline().strip())
for iii in range(t):
    n,k = [int(x) for x in stdin.readline().strip().split() ]
    s = [1,n+2]
    for i in range(k):
        mmax,mmin,pos = -1,-1,-1
        for j in range(len(s)-1):
            if s[j]==s[j+1]+1: continue
            tpos = int((s[j]+s[j+1])/2)
            tmmax = max(abs(tpos-s[j]),abs(tpos-s[j+1]))
            tmmin = min(abs(tpos-s[j]),abs(tpos-s[j+1]))
            if tmmin>mmin:
                mmin=tmmin
                mmax=tmmax
                pos = tpos
            elif tmmin==mmin and tmmax>mmax:
                mmax=tmmax
                pos = tpos
        s.append(pos)
        s.sort()
    print('Case #{0}: {1} {2}'.format(iii+1,mmax-1,mmin-1))
        
