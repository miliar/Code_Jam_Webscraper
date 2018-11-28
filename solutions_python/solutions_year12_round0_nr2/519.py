def solve_tc(wc, p, lv):

    s = len([x for x in lv if sure(p, x)])
    w = [x for x in lv if not sure(p, x)]
    #import pdb; pdb.set_trace()
    w = [x for x in w if wierd(p, x)]
    
    s += min(len(w), wc)
    return s
    
def sure(p, v):
    for x in xrange(10, p-1, -1):
        if (2*x + x + 1 == v):
            return True
        if (2*x + x - 1 == v) and ((x-1) >= 0):
            return True
        if (3*x == v):
            return True
    if ((2*(p-1) + p) == v) and ((p-1) >= 0):
        return True
    else:
        return False
        
def wierd(p, v):
    for x in xrange(10, p-1, -1):
        if (2*x + (x-2) == v) and ((x-2) >= 0):
            return True
        if (x + (x-2)*2 == v) and ((x-2) >= 0):
            return True
        if (3*x - 3 == v) and ((x-2) >= 0):
            return True
    return False
    
def load(filename):
    l = open(filename).readlines()
    l = l[1:]
    l = [line.split(' ', 3)[1:] for line in l]
    l = [[int(x), int(y) , z.split(' ')] for (x, y, z) in l]
    
    for e in l:
        for param in range(len(e[2])-1):
            e[2][param] = int(e[2][param])
        e[2][-1] = int((e[2][-1])[:-1])         
    return l
    
def solve(filename, outputfilename):
    l = load(filename)
    f = open(outputfilename, "w")
    
    for n,line in enumerate(l):
        f.write("Case #" +  str(n+1) + ": " + str(solve_tc(*line)) + '\n')
    
    f.close()
