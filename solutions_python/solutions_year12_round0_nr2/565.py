import sys
fh = open(sys.argv[1],"r")
T = int(fh.readline())
for i in xrange(T):
    v = map(int, fh.readline().rstrip().split(" "))
    N = v[0]
    S = v[1]
    p = v[2]
    r = 0
    for j in xrange(N):
        a, b = divmod(v[3+j], 3)
        if b == 0:
            if a>=p:
                r+=1
            elif a+1>=p and a-1>=0 and S>0:
                r+=1
                S-=1
        if b==1:
            if a+1>=p:
                r+=1
        if b ==2:
            if a+1>=p:
                r+=1
            elif a+2>=p and S>0:
                r+=1
                S-=1
    print "Case #{0}: {1}".format(i+1, r)
fh.close()
    
