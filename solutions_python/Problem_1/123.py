filename = "A-large.in"
f = open(filename, 'r')
of = open("A-large.out", 'w')

N = int(f.readline())

for i in xrange(N):
    S = int(f.readline())
    engines = {}
    for j in xrange(S):
        engines[f.readline()] = 0
    Q = int(f.readline())
    counter = 0
    switches = 0
    for j in xrange(Q):
        query = f.readline()
        if(engines[query] == 0):
            engines[query] = 1
            counter += 1
        if(counter == S):
            switches += 1
            counter = 1
            for k in engines:
                engines[k] = 0
            engines[query] = 1
    print >> of, "Case #%d: %d" % (i + 1, switches)
f.close()
of.close()
