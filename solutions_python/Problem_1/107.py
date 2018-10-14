import sys

def masLejos(engines, queries):
    mas = 0
    for eng in engines:
        newp = queries.index(eng)
        if newp > mas:
            mas = newp
    return mas

def proc(engines, queries):
#    print "eng!", engines
    cant = 0
    while True:
        try:
#            print "aver", queries
            pos = masLejos(engines, queries)
            queries = queries[pos:]
            cant += 1
        except ValueError:
            return cant

archinp = open(sys.argv[1])
canttests = int(archinp.readline())

for numtest in xrange(1,canttests+1):
    cantengines = int(archinp.readline())
    engines = [archinp.readline().strip() for x in xrange(cantengines)]
    cantqueries = int(archinp.readline())
    queries = [archinp.readline().strip() for x in xrange(cantqueries)]
    result = proc(engines, queries)
    print "Case #%d: %d" % (numtest, result)
