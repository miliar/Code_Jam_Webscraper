f = open("inp2", "r")
t = int(f.readline())
for tt in range(1,t+1):
    print "Case #"+str(tt)+":",
    a = map(int,f.readline().split())
    n = a[0]; s = a[1]; p = a[2]; a = a[3:]
    p = max(p*3-2,0); pp = max(0,p-2); c = 0; cc = 0
    for aa in a:
        if aa==0:
            if p==0:
                c+=1
        elif aa==1:
            if p==1:
                c+=1
        elif aa>=p:
            c+=1
        elif aa>=pp:
            cc+=1
    c+=min(cc,s)
    print c
