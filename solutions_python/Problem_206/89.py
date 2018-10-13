
f = open("1.in")

num_test = int(f.readline())

for iter_test in xrange(num_test):
    line = f.readline()
    d, n = map(int, line.split())
    m = 0
    for _ in xrange(n):
        k, s = map(int, f.readline().split())
        #print k, s
        cm = (d - k) * 1.0 / s
        #print cm
        if cm > m:
            m = cm
    

    print "Case #%d:"%(iter_test + 1),
    print "%0.7f"%(d / m)
