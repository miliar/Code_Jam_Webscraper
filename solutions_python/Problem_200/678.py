def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

def testcase(cas=-1):
    N = readval()
    def is_tidy(n): 
        s = str(n)
        for i in xrange(len(s)-1):
            if int(s[i])>int(s[i+1]): return False
        return True 
    n = N 
    res = ''
    while is_tidy(n) is False: 
        k = n%10
        n -= (k+1)%10
        res = '9'+res 
        n /= 10 
    res = str(n) + res 
    print 'Case #%d: %d' % ( cas, int(res) )

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)
