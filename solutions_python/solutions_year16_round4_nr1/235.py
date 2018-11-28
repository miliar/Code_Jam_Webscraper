def backwards(c, depth):
    if c == 'P':
        return 'PR'
    elif c == 'R':
        if depth >= 2:
            return 'SR'
        return 'RS'
    else:
        if depth >= 3:
            return 'SP'
        return 'PS'

def solve(R, P, S, depth):
    if R+P+S == 1:
        if R==1: return 'R'
        if P==1: return 'P'
        return 'S'

    RP = (R+P-S)/2
    PS = (P+S-R)/2
    SR = (S+R-P)/2

    if RP < 0 or PS < 0 or SR < 0:
        return None

    sub = solve(SR, RP, PS, depth+1)
    if sub is None:
        return None

    return "".join([backwards(c, depth+1) for c in sub])

with open("a.in") as f:
    t = int(next(f))
    for case in xrange(t):
        N, R, P, S = [int(s) for s in next(f).strip().split(" ")]

        x = solve(R, P, S, 0)
        print "Case #{}: {}".format(case+1, x or "IMPOSSIBLE")
