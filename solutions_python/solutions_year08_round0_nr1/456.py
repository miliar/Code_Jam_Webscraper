import sys

def getln():
    return sys.stdin.readline().strip()

n_cases = int(getln())

for case in range(1, n_cases+1):
    n_engines = int(getln())
    engines = dict((getln(), False) for i in range(n_engines))
    n_searches = int(getln())
    searches = [getln() for i in range(n_searches)]

    n = 0
    count = 0
    for search in searches:
        if not engines[search]:
            engines[search] = True
            n += 1
        if n == n_engines:
            count += 1
            n = 1
            for key in engines:
                engines[key] = False
            engines[search] = True

    print "Case #%d: %d"%(case, count)

    
