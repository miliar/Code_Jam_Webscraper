import sys
inp=open("input.txt","r")
out=open("output.txt","w")
sys.stdin=inp
sys.stdout=out
t=int(raw_input())
for test in xrange(t):
    n,s=raw_input().strip().split()
    n=int(n)
    cnt_stood=0
    cost=0
    for i in xrange(len(s)):
        if cnt_stood>=i:
            cnt_stood+=int(s[i])
        elif s[i]!='0':
            #print i,cnt_stood
            cost+=(i-cnt_stood)
            cnt_stood+=(i-cnt_stood)+int(s[i])
    print 'Case #' +str(test+1) +': '+str(cost)
inp.close()
out.close()
