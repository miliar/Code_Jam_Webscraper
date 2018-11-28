T = int(raw_input())

for i in xrange(1, T+1):
    N, M = (int(x) for x in raw_input().split(" "))
    s = set()
    def add(path):
        c = path.split("/")
        b = ""
        for comp in c:
            b = "%s/%s" % (b, comp)
            s.add(b)
    for j in range(N):
        add(raw_input())
    initial_dirs = s.copy()
    for j in range(M):
        add(raw_input())
    print "Case #%i: %i" % (i, len(s - initial_dirs - set(["/"])))
    
