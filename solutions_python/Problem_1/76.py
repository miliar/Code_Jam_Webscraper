import sys

for case in range(1, int(sys.stdin.readline())+1):
    engines = []
    for i in range(0, int(sys.stdin.readline())):
        engines.append(sys.stdin.readline())
    queries = []
    for i in range(0, int(sys.stdin.readline())):
        queries.append(sys.stdin.readline())

    switch = 0
    while len(queries) > 0:
        maxpos = 0
        for e in engines:
            try:
                epos = queries.index(e)
            except ValueError:
                maxpos = len(queries)
                break
            if epos > maxpos:
                maxpos = epos
        if(maxpos < len(queries)):
            switch = switch + 1
        queries = queries[maxpos:]
    
    print "Case #%d: %d" % (case, switch)
