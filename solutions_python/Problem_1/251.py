import sys

def Partition(n, l):
    res = []

    if len(l) > 0 and l[0] != 1:
        res.append((1, l[0] - 1))

    for i in range(1, len(l)):
        p = l[i - 1]
        q = l[i]
        if q - p > 1:
            res.append((p + 1, q - 1))

    if len(l) > 0 and l[-1] < n:
        res.append((l[-1] + 1, n))

    return res

def Max(pairs):
    if len(pairs) == 0:
        return ()

    res = pairs[0]
    for pair in pairs[1:]:
        if pair[1] > res[1]:
            res = pair
    return res

def ChooseEngines(engines, queries):
    engine2Queries = {}

    for engine in engines:
        engine2Queries[engine] = []

    for i, query in enumerate(queries):
        engine2Queries[query].append(i + 1)
        
    for engine in engines:
        if len(engine2Queries[engine]) == 0:
            return [engine]
        
    #print engine2Queries
    
    engine2Requests = {}
    for engine in engines:
        engine2Requests[engine] = Partition(len(queries), engine2Queries[engine])
        
    #print engine2Requests
    
    res = []
    q = 1
    while q <= len(queries):
        requests2Engine = {}
        
        for engine in engines:
            for request in engine2Requests[engine]:
                if q >= request[0] and q <= request[1]:
                    requests2Engine[request] = engine

        requests = requests2Engine.keys()
        #print q, requests, "\n"
        if len(requests) > 0:
            request = Max(requests)
            res.append(requests2Engine[request])
            q = request[1] + 1
        else:
            break
    #print res
    return res

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)
        
    fin = open(sys.argv[1], "r")
    inCases = int(fin.readline().strip())
    
    for i in range(1, inCases + 1):
        S = int(fin.readline().strip())
        engines = []
        for s in range(0, S):
            engines.append(fin.readline().strip())

        Q = int(fin.readline().strip())
        queries = []
        for q in range(0, Q):
            queries.append(fin.readline().strip())
            
        res = ChooseEngines(engines, queries)
        print "Case #%d: %d" % (i, max(len(res) - 1, 0))

    fin.close()