def readint():
    return int(raw_input())

def istidy(n):
    prv = None
    
    for ch in str(n):
        if prv is not None and prv > ch:
            return False
        prv = ch
    return True
    
def solve(n):
    for i in xrange(n, 0, -1):
        if istidy(i):
            return i
    return 0
            
def run():
    N = readint()
    for i in range(N):
        x = solve(readint())
        print 'Case #%d: %d' % (i+1, x)
        
run()