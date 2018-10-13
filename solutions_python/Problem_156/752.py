def solve(P):
    t = 0
    r = max(P)
    while max(P)>1:
        
        p1 = max(P)
        if(p1==9):
            pp = P[:]
            pp.append(3)
            pp.append(3)
            ind = pp.index(p1)
            pp[ind] -= 6
            s = solve(pp)
            r = min(r, t+2+s)
        p2 = p1/2
        
        t += 1
        P.append(p2)
        ind = P.index(p1)
        P[ind] -= p2
        
        r = min(r, t+max(P))
    return r

T = int(raw_input())
for i in range(T):
    r = 0
    D = int(raw_input())
    P = [int(j) for j in raw_input().split()]
    r = solve(P)

    print"Case #"+str(i+1)+": "+str(r)
