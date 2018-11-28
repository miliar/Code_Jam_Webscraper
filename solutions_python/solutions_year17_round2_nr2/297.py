def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

def testcase(cas=-1):
    N, R, O, Y, G, B, V = readvals() 
    # small case: only have RYB
    nbCh = sorted([(R,'R'),(Y, 'Y'), (B, 'B')])
    nb,Ch = zip(*nbCh)
    a,b,c = nb # a <= b <= c
    A,B,C = Ch

    CAs = ''
    diff = c-b-1
    if diff > 0: # try to make c-b <= 1
        if diff <= a: # use A to consumm C
            CAs = (C+A)*diff
            a-=diff; c-=diff 
        else: 
            print 'Case #%d: %s' % ( cas, 'IMPOSSIBLE' )
            return 
    def solve(b,c): # give a correct config of BC *in a line*
        if c-b > 1: return None # IMPOSSIBLE
        else: return (C+B)*b + C*(c-b)
    line = solve(b-a, c-a)
    if line is None or (a==0 and line[0]==line[-1]): 
        print 'Case #%d: %s' % ( cas, 'IMPOSSIBLE' )
        return 
    # line is like 'CBCB' or 'CBCBC'
    res = line + (A+C+B)*a # answer should be 'C...B'
    res += CAs # add 'C...A'
    print 'Case #%d: %s' % ( cas, res )

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)
