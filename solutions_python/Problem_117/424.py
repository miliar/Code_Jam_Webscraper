for i in range(int(raw_input())):
    n,m=map(int,raw_input().split(" "))
    t=[]
    for j in range(n):
        t.append(map(int,raw_input().split()))
    v=0
    # print"nub"
    # print "n,m",n,m
    print"Case #"+str(i+1)+":",
    m1=[max(t[j][k] for k in range(m)) for j in range(n)]
    m2=[max(t[k][j] for k in range(n)) for j in range(m)]
    tt=[t[j][k]==m1[j] or t[j][k]==m2[k] for j in range(n) for k in range(m)]
    if(all(tt)):
        print "YES"
    else:
        print "NO"
