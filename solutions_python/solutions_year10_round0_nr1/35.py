import sys
fin = open(sys.argv[1], 'r')

T = int(fin.readline())
for i in xrange(T):
    N, K = [int(x) for x in fin.readline().split()]
    
    on = (K & ((1<<N)-1)) == ((1<<N)-1)
    print 'Case #%d: %s' % (i+1, 'ON' if on else 'OFF')