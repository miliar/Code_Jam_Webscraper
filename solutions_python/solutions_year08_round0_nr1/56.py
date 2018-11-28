#!/usr/bin/python

#import mpmath
import copy
import sys
#import pp

def resolve(engines,queries):
    c = 0
    actuals = copy.deepcopy(engines)
    for query in queries:
        if query in actuals:
            actuals.remove(query)
#        print c
#        print query
#        print actuals

        if actuals.__len__()<1:
            c += 1
            actuals = copy.deepcopy(engines)
            actuals.remove(query)

    return "%d" % (c)


def read_in():
    fd = open("in")

    n = int(fd.readline())
    #parallel = pp.Server(ppservers=(),secret="")
    #threads = []
    out=[]

    for i in xrange(n):
        print "Create: %d       \r"%(i),
        sys.stdout.flush()

        ######

        S = int(fd.readline())
        engines=[]
        for j in xrange(S):
            engines.append(fd.readline())

        Q = int(fd.readline())
        queries = []
        for j in xrange(Q):
            queries.append(fd.readline())

#        resolve(engines,queries)

        #func = resolve
        #args = (None,)
        #depfuncs = (None,)
        #depmodules = (None,)
        ######

        out.append("Case #%d: %s"%(i+1,resolve(engines,queries)))
        #out.append("Case #%d: %s"%(i+1,threads[i]()))

        #threads.append(parallel.submit(func,args,depfuncs,depmodules))


    #print "\n"
    #for i in xrange(threads.__len__()):
    #    print "Join: %d           \r"%(i+1),
    #    sys.stdout.flush()

    return "\n".join(out)



print read_in()

