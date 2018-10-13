import sys, math
s = sys.stdin.readlines()
T = int(s[0])
i = 1

for xx in xrange(T):
    N = int(s[i])
    X=[]
    Y=[]
    R=[]
    i+=1

    for z in xrange(N):
        x,y,r = map(int, s[i].split())
        X.append(x)
        Y.append(y)
        R.append(r)
        i+=1

    def get_rad(i1,i2):
        return (math.sqrt(math.pow(X[i1]-X[i2],2)+math.pow(Y[i1]-Y[i2],2))+R[i1]+R[i2]) / 2

    if N>3:
        print "Case #%s: %F" %(xx+1, sum(R))
    elif N==1:
        print "Case #%s: %F" %(xx+1, R[0])
    elif N==2:
        print "Case #%s: %F" %(xx+1, max(R))
    elif N==3:
        r1 = get_rad(0,1)
        r2 = get_rad(0,2)
        r3 = get_rad(1,2)
        res=[]
        if r1>=R[2]:
            res.append(r1)
        if r2>=R[1]:
            res.append(r2)
        if r3>=R[0]:
            res.append(r3)
        print "Case #%s: %F" %(xx+1, min(res))
