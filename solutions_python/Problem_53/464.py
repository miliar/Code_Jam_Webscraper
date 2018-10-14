def p(str):
		#print str
		pass


def readline():
    import sys
    f = open(sys.argv[1])
    T = int(f.readline()[:-1])
    p(T)
    str = [ "OFF", "ON" ]
    for t in range(T):
        N, K = f.readline()[:-1].split()
        N = int(N)
        K = int(K)
        p(N)
        p(K)
        s = snapper(N,K)
        print "Case #%d: %s" % (t+1, str[s])

def snapper(N,K):
    p( K % 2 **N)
    return ( K % (2 ** N) == 2**N-1)

readline()
