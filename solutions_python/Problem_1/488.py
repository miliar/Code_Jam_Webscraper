#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

#f = open('A-test.in')
#g = open('A-test.out', 'w')

#f = open('A-small-attempt0.in.txt')
#g = open('A-small.out', 'w')

f = open('A-large.in.txt')
g = open('A-large.out', 'w')

runs = int(f.readline()[:-1])

for i in range(runs):
    
    numengines = int(f.readline()[:-1])
    engines = []
    for j in range(numengines):
        engines.append(f.readline()[:-1])
    numsearches = int(f.readline()[:-1])
    searches = []
    for j in range(numsearches):
        searches.append(f.readline()[:-1])

    switches = 0
    available = [x for x in engines]
    for query in searches:
        if query in available:
            available.remove(query)
        if not available:
            switches += 1
            available = [x for x in engines]
            available.remove(query)
            print 'use %s' % query
    print 'use %s' % available

    print >> g, "Case #%d: %d" % (i+1, switches)
    print "Case #%d: %d (e=%d s=%d) " % (i+1, switches, numengines, numsearches)


g.close()
f.close()
