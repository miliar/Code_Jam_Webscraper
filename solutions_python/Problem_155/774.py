z=0
for _ in xrange(input()):
    n,s=raw_input().split()
    n=int(n)
    a=0
    c=int(s[0])
    for i in xrange(1,n+1):
        a=max(a,max(i-c,0))
        c+=int(s[i])
    z+=1
    ans="Case #"+str(z)+": "+str(a)
    print ans
