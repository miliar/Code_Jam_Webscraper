
# imports
import sys
import os


def Main():
    datafile = os.path.basename(__file__).replace('.py', '.txt')
    resultsfile = os.path.basename(__file__).replace('.py', '_results.txt')

    data = [] 
    with open(datafile) as f:
        data = f.readlines()

    idx = 0
    numtests = int(data[idx].strip())
    idx = idx + 1

    print 'numtests = %d' % numtests

    linespertest = 1

    sys.setrecursionlimit(100000)

    limit = 10000

    print '-'*30
    results = []
    for i in range(numtests):
        print '-'*20

        farmcost, cookierate, targetcount = data[idx + i * linespertest].split()
        farmcost, cookierate, targetcount =  float(farmcost), float(cookierate), float(targetcount)
        print farmcost, cookierate, targetcount 

        # -- this calculates the time needed to get to each production level

        # -- this fails, too much recursion
        #x = lambda f, c, offset, idx: f / (2 + c*idx) + x(f, c, offset, idx-1) if idx > 1 else f / (2 + c*idx)  

        f = farmcost
        c = cookierate
        t = targetcount
        cr = lambda index: 2 + c * index

        print '-'*20
        print 'time to each collection level'
        print '-'*20

        # -- the time to each production level
        lastoffset = 0
        funcs = []
        for ti in range(limit):
            #lastoffset = funcs[-1]() if i else 0
            #print 'lastoffset %f ' % lastoffset

            if ti == 0:
                funcs.append(lambda: 0)
            else:
                # -- force lastoffset and i to be captured in the closure
                funcs.append(lambda lastoffset=lastoffset, ti=ti: f / (cr(ti-1)) + lastoffset)

            #print f 
            #print cr(i-1)
            #print lastoffset

            #print f / cr(i-1) + lastoffset if i else 0
            lastoffset = funcs[-1]() 
            #print funcs[-1]()

            
        #print '-'*20
        ## -- verify, this is the same
        #for i in range(limit):
            ##lastoffset = funcs[-1]() if i else 0
            #print funcs[i]()
        #break

        print '-'*20
        print 'collection rate per level'
        print '-'*20

        # -- cookie rates per level
        #cr = []
        #for i in range(limit):
            ##cr_ = 2 + c*i
            ##print cr(i)
            #pass
            ##cr.append(lambda: 2 + c*i)

        print '-'*20
        print 'time to cookie'
        print '-'*20

        # -- time to cookie count at each level
        ttc = []
        for ti in range(limit):
            ttc.append(t/cr(ti) + funcs[ti]())

        #print '\n'.join([str(t) for t in ttc])

        #print '\n\n'
        print min(ttc)

        #a = [x(farmcost, cookierate, 0, i) for i in range(10000)]
        #print x(farmcost, cookierate, 0, 10)

        results.append('Case #%d: %.7f' % (i+1, min(ttc)))
    
    print '-'*30

    with open(resultsfile, 'w') as f:
        f.write('\n'.join(results))

    return 0

if __name__ == "__main__":
    sys.exit(Main())
