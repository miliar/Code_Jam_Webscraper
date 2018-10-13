def dist(a, b):
    ai, bi = 0, 0
    ap, bp = "", ""
    steps = 0
    while ai < len(a) and bi < len(b):
        ap = a[ai]
        ac = 0
        while ai < len(a) and a[ai] == ap:
            ai += 1
            ac += 1
        
        bp = b[bi]
        bc = 0
        while bi < len(b) and b[bi] == bp:
            bi += 1
            bc += 1
        
        if ap != bp:
            return -1
        
        steps += abs( ac - bc )
    
    if ai < len(a) or bi < len(b):
        return -1
    return steps

def matches(S):
    rmin, rmax = "", ""
    si = [0]*len(S)
    stop = False
    
    while not stop:
        sp = S[0][si[0]]
        mn, mx = -1, 0
        for i in range(len(S)):
            csp = S[i][si[i]]
            cc = 0
            while si[i] < len(S[i]) and S[i][si[i]] == csp:
                si[i] += 1
                cc += 1
            
            stop = stop or si[i] == len(S[i])
            
            if sp != csp:
                return "", ""
            mn = min( mn, cc ) if mn >= 0 else cc
            mx = max( mx, cc )
        rmin += sp*mn
        rmax += sp*mx
        
    for i in range(len(S)):
        if si[i] < len(S[i]):
            return "", ""
    
    return rmin, rmax        

T = int( input() )
for Ti in range( 1, T+1 ):
    N = int( input() )
    S = [ input() for Ni in range(N) ]
    r = [0]*N
    for Si in range(N):
        for Sj in range( Si+1, N ):
            d = dist( S[Si], S[Sj] )
            r[Si] += d
            r[Sj] += d

    mm = matches(S)
    for match in mm:
        mr = 0
        for Si in S:
            mr += dist( match, Si )
        r.append(mr)

    #print(r)
    result = min(r)
    print( "Case #{0}: {1}".format( Ti, result if result >= 0 else "Fegla Won" ) )