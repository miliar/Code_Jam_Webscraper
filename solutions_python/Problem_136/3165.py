T = int(raw_input())
for i in range(T):
    C,F,X = map(float, raw_input().split())
    r=X/2
    t=C/2
    m=C
    v=2
    go = True
    if(C>X):
        go=False
    while go:
       tx=r
       miss=X-m
       missf=miss+C
       vf=v+F
       txf=t+missf/vf
       if txf<tx:
           # print t
           r=txf
           m=C
           t=t+C/vf
           v=vf
           # print 't',t
       else:
           # print t,r,txf, vf, miss
           go =False
    print "Case #"+str(i+1)+":",r
