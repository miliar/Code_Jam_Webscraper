def get_split(enum, onum):
    if enum != 0:
        tmp = enum
        if (enum/2)%2 == 0:
	    enum = enum/2
	    onum = tmp/2 - 1
	else:
	    enum = enum/2 - 1
	    onum = tmp/2
    else:
        if ((onum-1)/2)%2 == 0:
	    enum = (onum-1)/2
	    onum = 0
	else:
	    onum = (onum-1)/2
	    enum = 0
    return (enum, onum)

def get_res(N, K):
        if N%2 == 0:
            enum = N
	    onum = 0
	    e = 1
	    o = 0
	else:
	    enum = 0
	    onum = N
	    e = 0
	    o = 1
	Sprev = 0
	eprev = 0
	oprev = 0
	S = e+o
        #print "e o S Sprev N enum onum"
        while K > S:
            #print e, o, S, " ", Sprev, " ", N, " ", enum, "  ", onum
	    oprev = o
	    eprev = e
            if (onum/2)%2 == 0:
	        o = eprev
	        e = eprev + 2*oprev
	    else:
	        o = 2*oprev + eprev
		e = eprev
	    Sprev = S
	    S += (e + o)
            #print "# enum-in, onum-in: ", enum, onum
	    enum, onum = get_split(enum, onum)
            #print "# enum-out, onum-out: ", enum, onum
	    N /= 2
	
	kprime = K-Sprev
        #print "kprime: ", kprime
        #print "N e o:",  N, e, o
	if N % 2 == 0:
	    compare = e
	else:
	    compare = o
	
	if kprime > compare:
	    res = N-1
	else:
	    res = N
        #print "res: ", res, res%2	
	if res % 2 == 0:
	    y, z = res/2, max(0, (res/2-1))
            #print "y, z: ", y, z
	else:
	    y, z = res/2, res/2
        #print "y, z: ", y, z
	return (y, z)

t = int(raw_input())  
for i in xrange(1, t + 1):
    N, K = [int(s) for s in raw_input().split(" ")]
    y, z = get_res(N, K)
    print "Case #{}: {} {}".format(i, y, z)
