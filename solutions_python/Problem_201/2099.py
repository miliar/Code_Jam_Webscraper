import sys
#sys.setrecursionlimit(1000)

def boilerplate(filename):
    with open(filename, 'r') as infi:
        with open('output-'+filename, 'w') as outfi:
            numcases = infi.readline().strip()
            numcases = int(numcases)
            for i in range(numcases):
                case = infi.readline().strip()
                outfi.write(f(i, case)+'\n')

def tester(x):
    return f(0, x)

memoized = {}
def memoize(function):
    global memoized
    def output_function(*args):
        if args in memoized:
            return memoized[args]
        else:
            output = function(*args)
            memoized[args] = output
            return output
    return output_function

def bathrooms(casenumber, inp):
    n, k = map(int, inp.split(' '))
    stalls = [0] * n
    for i in range(k):
        most_recent_stall_at = -1
        els = []
        for j in range(n):
            if stalls[j] == 1:
                most_recent_stall_at = j
            els.append(j - most_recent_stall_at - 1)
        #print 'L',els, stalls

        most_recent_stall_at = -1
        ars = []
        for j in range(n):
            if stalls[n-j-1] == 1:
                most_recent_stall_at = j
            ars.insert(0, j - most_recent_stall_at - 1)
        #print 'R',ars, stalls


        pairs = zip(els, ars)
        minlrs = map(min, pairs)
        maxlrs = map(max, pairs)
        #print 'minlrs maxlrs', minlrs, maxlrs

        preindices = [i for i in range(n) if stalls[i] == 0]
        maxminlr = max([minlrs[i] for i in preindices])
        indices = [i for i, minlr in enumerate(minlrs) if minlr == maxminlr and stalls[i] == 0]
        #print 'indices', indices
        if len(indices) == 1:
            chosen = indices[0]
            maxlr = maxlrs[chosen]
            minlr = minlrs[chosen]
            assert stalls[chosen] == 0
            stalls[chosen] = 1
            #print 'chose', chosen
        else:
            maxmaxlr = max([maxlrs[i] for i in indices])
            indices2 = [i for i, maxlr in enumerate(maxlrs) if maxlr == maxmaxlr and i in indices]
            #print 'indices2', indices2
            chosen = indices2[0]
            maxlr = maxlrs[chosen]
            minlr = minlrs[chosen]
            stalls[chosen] = 1
            #print 'chose2', chosen


    return 'Case #%s: %s %s' % (casenumber+1, maxlr, minlr)

f = bathrooms
