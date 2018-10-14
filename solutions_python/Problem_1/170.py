
ifile = file('A-small-attempt1.in')

num = int(ifile.readline())

for i in xrange(num):
    numsearch = int(ifile.readline())
    
    engine = set()
    for j in xrange(numsearch):
        engine.add(ifile.readline().strip())
        
    numtest = int(ifile.readline())
    
    total = 0
    cache = set()
    for t in xrange(numtest):
        query = ifile.readline().strip()
        if query in cache:
            continue
        elif(query in engine):
            cache.add(query)
            
        if len(cache) == numsearch:
            total += 1
#            if token
#            token = query
            cache.clear()
            cache.add(query)
            
    print 'Case #%s: %s'%(i+1, total)
    