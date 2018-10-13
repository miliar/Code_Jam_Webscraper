memo = {}
engines = []
queries = []

def recurse(current, query):
    if memo.has_key((current,query)):
        return memo[(current,query)]
    
    if (query>len(queries)):
        return 0

    #print "evaluating : %s, %s" % (current, query)
    #raw_input()
    
    for qi in range(query,len(queries)):
        if queries[qi]==engines[current]:
            smin = 100000
            for i in range(len(engines)):
                if i==current:
                    continue
                s = 1 + recurse(i,qi)
                if s<smin:
                    smin = s
            memo[(current,query)] = smin
            return smin
    memo[(current,query)] = 0
    return 0
                
            
f = file("A-small-attempt0.in")
cases = int(f.readline(),10)

for i in range(cases):
    sec = int(f.readline(),10)
    engines = []
    for e in range(sec):
        engines.append(f.readline())

    qrc = int(f.readline(),10)
    queries = []
    for q in range(qrc):
        queries.append(f.readline())

    memo = {}
    smin = 100000
    for e in range(sec):
        s = recurse(e,0)
        if s<smin:
            smin = s
            
    print "Case #%s: %s" % (i+1,smin)
    
    
