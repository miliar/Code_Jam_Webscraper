import sys
import time
t = int(sys.stdin.readline())
for tt in  range(t):
    N = sys.stdin.readline().strip()
    d = [int(i) for i in N]
    c = len(d)-1
    while c > 0:
        if d[c] >= max(d[:c]):
            c=c-1
        else:
            for i in range(c,len(d)):
                d[i]=9
            c=c-1
            while d[c]==1 and c>=0:
                if c==0:
                    d[c]=0
                else:
                    d[c]=9
                    c=c-1
            if(d[c] > 0):
                d[c] = d[c] -1
    

    print "Case #" + str(1 + tt) + ": " + str(int("".join(str(dd) for dd in d)))
