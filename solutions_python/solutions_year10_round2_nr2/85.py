def makes_it(x,v,b,t):
    return float(b-x)/float(v) <= t

def handle_case(n,k,b,t,xs,vs):
    if k == 0:
        return 0
    blocks = lambda (x,v): makes_it(x,v,b,t)
    good = map(blocks, reversed(zip(xs,vs)))
    swaps = 0
    bad = 0
    found = 0
    for b in good:
        if b:
            swaps += bad
            found += 1
        else:
            bad += 1
        if found == k:
            return swaps
    return None

def parse_cases(infile):
    c = int(infile.readline())
    for i in xrange(c):
        n,k,b,t = map(int,infile.readline().split())
        xs = map(int,infile.readline().split())
        assert len(xs) == n
        vs = map(int,infile.readline().split())
        assert len(vs) == n
        #print n,k,b,t,xs,vs
        ret = handle_case(n,k,b,t,xs,vs)
        if ret is None:
            out = "IMPOSSIBLE"
        else:
            out = str(ret)
        print "Case #%d: %s" % (i+1,out)

if __name__ == '__main__':
    import sys
    import StringIO
    
    s = """3
5 3 10 5
0 2 5 6 7
1 1 1 1 4
5 3 10 5
0 2 3 5 7
2 1 1 1 4
5 3 10 5
0 2 3 4 7
2 1 1 1 4"""
    if len(sys.argv) == 2:
        infile = open(sys.argv[1])
    else:
        infile = StringIO.StringIO(s)
    parse_cases(infile)
    infile.close()
