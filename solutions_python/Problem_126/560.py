con="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
cach={}
def f(st,n,(v,b)):
    if len(st)<n:
        return 0
    if (v,b) in cach.keys():
        #print(v,b)
        #print st
        return f(st[1:],n,(v+1,b)) + f(st[:-1],n,(v,b+1))
    cach[(v,b)]=True
    chk=False
    for i in range(len(st)-n+1):
        m=True
        for j in range(n):
            if not(st[i+j] in con):
                m=False
        if m:
            chk=True
            break
    if chk:
        #print st
        return 1 + f(st[1:],n,(v+1,b)) + f(st[:-1],n,(v,b+1))
    return f(st[1:],n,(v+1,b)) + f(st[:-1],n,(v,b+1))
t=input()
for y in range(t):
    s,n=raw_input().split(" ")
    n=int(n)
    cach={}
    k=0
    for x in range(len(s)):
        o = x
        for j in range(1,len(s[x:])+1):
            st= s[o:o+j]
            chk=False
            for i in range(len(st)-n+1):
                m=True
                for j in range(n):
                    if not(st[i+j] in con):
                        m=False
                if m:
                    chk=True
                    break
            if chk:
                k+=1
    print "Case #"+str(y+1)+": "+str(k)
