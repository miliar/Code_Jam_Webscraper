def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

def testcase_bfs(cas=-1):
    S, K = readvals(str)
    k = int(K)
    L = len(S)
    fine = '+' * L
    def flip(s, i): 
        assert 0<=i<=L-k
        s2 = list(s)
        for j in xrange(k): 
            s2[i+j] = '-' if s[i+j]=='+' else '+'
        s2 = ''.join(s2)
        # print 'flip(%s,%d)=%s' % (s, i, s2)
        return s2 
    # do a bfs
    visited = set()
    layer = set([S])
    step = 0 
    while layer: 
        # print layer
        visited.update(layer)
        newlayer = set() 
        for s in layer: 
            if s==fine: 
                print 'Case #%d: %d' % ( cas, step )
                return 
            for i in xrange(L-k+1): 
                s2 = flip(s, i)
                if s2 not in visited: 
                    newlayer.add(s2)
        layer = newlayer
        step += 1 
    print 'Case #%d: IMPOSSIBLE' % ( cas )

def testcase(cas=-1):
    S, K = readvals(str)
    k = int(K); L = len(S)
    s = list(S) 
    steps = 0 
    for i in xrange(L-k+1): 
        if s[i]=='+': continue 
        # if s[i] is '-', flip it 
        for j in xrange(k): 
            s[i+j] = '-' if s[i+j]=='+' else '+'
        steps += 1
    fine = '+' * L
    S = ''.join(s) 
    res = str(steps) if fine==S else 'IMPOSSIBLE'
    print 'Case #%d: %s' % (cas, res) 

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)
