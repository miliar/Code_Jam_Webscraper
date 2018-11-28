n=input()
for j in range(n):
    c=d=0
    p=raw_input().split()
    m,s=int(p[0]), p[1]
    for i in range(len(s)):
        e=int(s[i])
        if c<i and e>0:
            d+=i-c
            c+=d
        c+=e
    print "Case #"+str(j+1)+":", d
