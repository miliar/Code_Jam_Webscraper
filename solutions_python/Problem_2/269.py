import sys
n=int(sys.stdin.readline().strip())
for c in range(1,n+1):
    t=int(sys.stdin.readline().strip())
    ns=sys.stdin.readline().split()
    na=int(ns[0])
    nb=int(ns[1])
    a0=[]
    a1=[]
    for i in range(na):
        s=sys.stdin.readline().split()
        s[0]=s[0].split(":")
        s[1]=s[1].split(":")
        a0=a0+[int(s[0][0])*60+int(s[0][1])]
        a1=a1+[int(s[1][0])*60+int(s[1][1])]
    b0=[]
    b1=[]
    for i in range(nb):
        s=sys.stdin.readline().split()
        s[0]=s[0].split(":")
        s[1]=s[1].split(":")
        b0=b0+[int(s[0][0])*60+int(s[0][1])]
        b1=b1+[int(s[1][0])*60+int(s[1][1])]
    a0.sort()
    a1.sort()
    b0.sort()
    b1.sort()
    j=0
    for i in a1:
        while(j<len(b0)):
            if b0[j] >=i+t:
                b0.pop(j)
                break
            else:
                j=j+1
        if j>=len(b0): break
    j=0
    for i in b1:
        while(j<len(a0)):
            if a0[j] >= i+t:
                a0.pop(j)
                break
            else:
                j=j+1
        if j>=len(a0): break
    print "Case #"+str(c)+":",len(a0),len(b0)
