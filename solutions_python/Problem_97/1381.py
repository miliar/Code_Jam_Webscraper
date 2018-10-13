def get_combinations(val):
    combinations = []
    l = len(val)
    val = val + val
    for i in range(l):
        combinations.append(val[i:l+i])
    return combinations
        
def calculateDistinctPairs(a, b):
    found = set()
    
    cb = b
    
    while cb > a:
        sb = str(cb)
        to_test = get_combinations(sb)
        for t in to_test:
            alt = int(''.join(t))
            if alt >= a and alt < cb:
                found.add((alt, cb))
        cb = cb - 1
    return len(found)

for case in xrange(input()):
    inp = raw_input().split()
    
    min_val = int(inp[0])
    max_val = int(inp[1])
    
    res = calculateDistinctPairs(min_val, max_val)

    print "Case #%i: %i" % (case+1, res)
    