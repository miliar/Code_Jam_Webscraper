import sys



filename = sys.argv[1]

input = open(filename,'r')



T = map(int,input.readline().split())[0]



for i in range(1,T+1):
    
    result = 0
    a,b,k = map(long,input.readline().split())
    comb = []
    for a1 in xrange(a):
        for a2 in xrange(b):
            comb+=[(a1&a2)]

    for k1 in xrange(k):
        result += comb.count(k1)
    print "Case #%i: %i"%(i,result)


input.close()