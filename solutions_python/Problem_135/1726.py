from sets import Set
with open("in",'r') as f:
    T = int(f.readline())
    for t in xrange(T):
        res = []
        for i in xrange(2):
            a = int(f.readline())
            for j in xrange(a-1):
                f.readline()
            res.append(f.readline().split())
            for j in xrange(4-a):
                f.readline()
        X = Set(res[0])
        Y = Set(res[1])
        Z = X & Y
        res = "Case #%d: " % (t+1)
        if len(Z) == 1:
            res += "%s" % list(Z)[0]
        elif len(Z) > 1:
            res += "Bad magician!"
        else:
            res += "Volunteer cheated!"
        print res
            
