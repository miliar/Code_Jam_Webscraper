import sys, string

INFINITY = 999999999

f = open(sys.argv[1])
a = f.readlines()
f.close()

TC = int(a[0])
line = 1
for tc in xrange(TC):
    N = int(a[line])
    line += 1
    engines = map(string.strip, a[line:line+N])
    line += N
    Q = int(a[line])
    line += 1
    queries = map(string.strip, a[line:line+Q])
    line += Q
 
    answer = 0
    if Q==0:
        print 'Case #%d: %d'% (tc+1, answer)
        continue
    maxi = 0
    curr = 0
    iter = 0
    while curr<len(queries):
        maxi = 0
        for engine in engines:
            i = curr
            while i<len(queries):
                if queries[i]==engine:
                    break
                i += 1
            maxi = max(i, maxi)
        curr = maxi
        if curr<len(queries):
            iter += 1
        #print curr, len(queries)
    print 'Case #%d: %d'% (tc+1, iter)
    #print engines
    #print queries
    #print '*'*100
    