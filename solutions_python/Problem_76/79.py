f = open("C-large.in")
fout = open("C.out", "w")

T = int(f.readline())
for t in xrange(T):
    N = int(f.readline())
    values = map(int, f.readline().split())
    
    if reduce(lambda x, y: x^y, values) != 0:
        print >>fout, "Case #%d: NO" % (t+1, )
    else:    
        print >>fout, "Case #%d: %d" % (t+1, sum(values) - min(values))


    