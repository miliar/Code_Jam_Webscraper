fin = open("A-large.in", "r")
fout = open("A-large.out", "w")

def allsubdirs(path):
    path = path.split("/")
    for end in xrange(1, len(path) + 1):
        yield "/".join(path[:end])

T = int(fin.readline())

for t in xrange(T):
    N, M = [int(i) for i in fin.readline().split()]
    old = set([""])
    new = set([])
    
    for n in xrange(N):
        for d in allsubdirs(fin.readline().rstrip()):
            old.add(d)
    for m in xrange(M):
        for d in allsubdirs(fin.readline().rstrip()):
            new.add(d)

    #print len(new - old)
    fout.write("Case #%i: %i\n" % (t + 1, len(new - old)))

fin.close()
fout.close()
