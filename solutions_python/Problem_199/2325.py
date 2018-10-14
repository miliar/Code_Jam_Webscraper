import sys
import time
t = int(sys.stdin.readline())
for tt in  range(t):
    s,k=sys.stdin.readline().split()
    kk=int(k)
    ss=list(s)
    p=0
    r=0
    possible=1
    while p < len(ss):
        if ss[p]=="+":
            p+=1;
        elif len(ss) - p < kk:
            possible=0
            break
        else:
            r+=1
            for i in range(p, kk+p):
                if ss[i]=="+":
                    ss[i]="-"
                else:
                    ss[i]="+"

    result= "Case #" + str(1 + tt) + ": "
    if possible==0:
        print result + "IMPOSSIBLE"
    else:
        print result + str(r)
