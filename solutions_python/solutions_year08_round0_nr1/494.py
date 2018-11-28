# Problem A, Greedy algorithm

fin = open('A.in', 'r')
fout = open('A.out', 'w')

numcases = int(fin.readline())

for casenum in range(numcases):
    numengines = int(fin.readline())
    engines = []
    # load search engine names
    for enginenum in range(numengines):
        engines.append(fin.readline().strip())
    numqueries = int(fin.readline())
    queries = []
    # load queries
    for querynum in range(numqueries):
        queries.append(fin.readline().strip())
    
    seendict = {}
    for e in engines:
        seendict[e] = False
    # Run through queries until we've seen each engine queried once,
    # forcing a switch
    switches = 0
    for q in queries:
        seendict[q] = True
        for engine in seendict:   # Check to see if some engine is still viable
            if not seendict[engine]:
                break  # OK, we're still good for now
        else:  # if all values are True, then...
            for key in seendict:
                seendict[key] = False   # reset everything, except
            seendict[q] = True          # the one just seen (we had to
            switches += 1               # switch AWAY from that engine)
    fout.write("Case #%d: %d\n" % (casenum+1, switches))
