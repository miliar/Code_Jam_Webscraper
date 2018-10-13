import sys
N = int(sys.stdin.readline())
for caseNumber in range(1,N+1):
    #loading search engines
    S = int(sys.stdin.readline())
    engines = []
    for engineNumber in range(S):
        engines.append(sys.stdin.readline().rstrip('\n'))
    #loading queries
    Q = int(sys.stdin.readline())
    queries = []
    for queryNumber in range(Q):
        queries.append(sys.stdin.readline().rstrip('\n'))
    #calculating result
    result = 0
    while queries != []:
        maxDist = 0
        for engine in engines:
            try:
                distForThisEngine = queries.index(engine)
            except Exception, msg:
                queries = []
                break
            if distForThisEngine > maxDist:
                maxDist = distForThisEngine
        #now I know I can go as far as maxDist with best engine
        queries = queries[maxDist:]
        if (queries != []):
            result += 1
    print 'Case #%s: %s' % (caseNumber, result)
