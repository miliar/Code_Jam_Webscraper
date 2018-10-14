t=input()
for x in range(0,t):
    n,s=raw_input().split()
    n=int(n)
    l=len(s)
    cnt=int(s[0])
    r=0
    for i in range(1,l):
        if int(s[i])>0:
            if cnt>=i:
                cnt+=int(s[i])
            else:
                r+=i-cnt
                cnt=cnt+r+int(s[i])
    print "Case #%d: %d" %(x+1,r)

