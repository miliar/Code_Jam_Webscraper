file = open("A-large.in")
    
o = dict([(True, 'ON'), (False, 'OFF')])

T = int(file.readline())
for t in xrange(T):
    (N, K) = map(int, file.readline().split(" "))
    
    print "Case #%i: %s" % (t+1, o[(K + 1) % (2**N) == 0])