def readInts():
    r = raw_input()
    s = r.split()
    if len(s) == 1:
        return int(s[0])
    return [int(ss) for ss in s]

def solve(L, P, C):
    if L * C >= P:
        return 0

    count = 1
    ll = L
    while ll * C < P:
        ll *= C
        count += 1
    
    if count != 1:
        c1 = count / 2
    else:
        c1 = count
    
    
    a1 = solve(L, L * C ** c1, C)
    a2 = solve(L * C ** c1, P, C)
    a = max(a1, a2) + 1
    
    if count % 2:
        b1 = solve(L, L * C ** (c1 + 1), C)
        b2 = solve(L * C ** (c1 + 1), P, C)
        b = max(b1, b2) + 1
        if b < a:
            a = b

    return a

def main():
    t = readInts()
    
    case = 1
    for i in xrange(t):
        L, P, C = readInts()
        
        count = solve(L, P, C)
        
        
        print 'Case #%d: %d' % (case, count)
        case += 1

if __name__ == '__main__':
    main()

