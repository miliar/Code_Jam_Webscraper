def f(N,R,O,Y,G,B,V):
    R -= G
    Y -= V
    B -= O
    
    r,y,b = sorted(((R,"R"),(Y,'Y'),(B,'B')))
    # cap letter is number, lowercase letter is letter
    
    W,w = b
    X,x = y
    Z,z = r
    # print W,X,Z
    count_runs = X+Z-W
    if count_runs < 0:
        return "IMPOSSIBLE"
    first_part = count_runs*(w+x+z)
    
    sp1 = w*(W-count_runs)
    sp2 = x*(X-count_runs) + z*(Z-count_runs)
    second_part = ""
    for i,j in zip(sp1,sp2):
        second_part += i+j
    
    result = first_part + second_part
    
    cG = (G and not R)
    cO = (O and not B)
    cV = (V and not Y)

    # if there is a secondary color whose primary color is not present
    if cG or cO or cV:
        # if more than one of the above is >0 then return impossible
        if (cG and cO) or (cG and cV) or (cV and cO):
            return "IMPOSSIBLE"
        # if result is not empty then return impossible  
        if result:
            return "IMPOSSIBLE"
    
    for primary,secondary,count in [
        ('R','G',G),
        ('B','O',O),
        ('Y','V',V)
    ]:
        pos = result.find(primary)
        result = result[:pos] + (primary+secondary)*count + result[pos:]
    return result
    
    
        
T = int(raw_input())
for i in xrange(1,T+1):
    print "Case #%d: %s" % (i, f(*map(int,raw_input().split())))
    
    # 5
    # 0
    # 1
    # 2
    # 11
    # 1692Square Brackets [ ] | English Club