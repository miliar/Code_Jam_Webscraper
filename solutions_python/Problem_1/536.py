import sys
f = file(sys.argv[1])
s = [line.strip() for line in f]
numCases = int(s[0])
i = 1
for caseNum in range(numCases):
    engineCount = int(s[i])
    i += 1
    engines = [line for line in s[i : i + engineCount]]
    i += engineCount
    queryCount = int(s[i])
    i += 1
    dp = [[0 for k in range(queryCount + 1)] for j in range(engineCount)]
    queries = [line for line in s[i : i + queryCount]]
    i += queryCount
    for q in range(queryCount):       
        for e in range(engineCount):
            dp[e][q + 1] += dp[e][q]
            if dp[e][q] > 500000:
                m = dp[e][q]
                for e2 in range(engineCount):
                    m = min(m, dp[e2][q])
                dp[e][q + 1] = m + 1 
            if queries[q] == engines[e]:
                dp[e][q + 1] = 10000000            
        dp[engines.index(queries[q])][q + 1] += 1
    m = 100000
    for e in range(engineCount):
        m = min(m, dp[e][queryCount]) 
    print "Case #%d: %d" % (caseNum + 1, m)
