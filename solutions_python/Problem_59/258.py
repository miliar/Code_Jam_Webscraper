fin = open('a.txt')
fout = open('a.out','w')
T = int(fin.readline())
for t in xrange(1,T+1):
    N,M = [int(i) for i in fin.readline().split()]
    exists = {}
    for tt in xrange(0,N):
        d = fin.readline().strip()[1:]
        exists[d] = 1
    c = 0
    for tt in xrange(0,M):
        d = fin.readline()[1:].strip().split('/')
        path = []
        for p in d:
            if p == "":
                continue
            path.append(p)
            s = "/".join(path)
            if s in exists:
                continue
            c+=1
            exists[s] = 1
    fout.write("Case #{0}: {1}\n".format(t,c))
            
    