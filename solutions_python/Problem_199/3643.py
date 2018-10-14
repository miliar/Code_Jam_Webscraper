def readint():
    return int(raw_input())

def readstr():
    return raw_input().strip()

def strmod(s, i, c):
    return s[:i] + c + s[i+1:]    
    
def run():
    N = readint()
    for i in range(N):
        x = readstr()
        pancakes, sz = x.split()
        sz = int(sz)
        print 'Case #%d: %s' % (i+1, solve(pancakes, sz))
    
def strip(p):
    i = 0
    L = len(p)
    for i in range(L):
        if p[i] == '-':
            break
    else:
        return ''
        
    p = p[i:]
    L = len(p)
    for j in range(L-1, -1, -1):
        if p[j] == '-':
            break
    else:
        return ''
        
    p = p[:j+1]
    return p
    
def solve(p, sz):
    rc = 0
    while p:
        p = strip(p)
        if not p:
            return rc
            
        if len(p) < sz:
            return 'IMPOSSIBLE'
        
        rc += 1
        for i in range(sz):
            if p[i] == '+':
                p = strmod(p, i, '-')
            else:
                p = strmod(p, i, '+')
    
    return rc
    
run()