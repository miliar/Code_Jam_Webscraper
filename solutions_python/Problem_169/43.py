def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret


def cal_V(C1, C2, X, V):
    # X = (V1C1 + V2C2) / (V1+V2)
    # V = V1 + V2 
    # V2 = (V - V * C1) / (C2 - C1)
    # wrong
    # V2 = (X * V - C1 * V) / (C2-C1)
    V2 = (X * V - C1 * V) / (C2-C1)
    #V2 = (V - V * C1) / (C2 - C1)
    V1 = V - V2
    return V1, V2


def solve(RCs, V, X):
    if len(RCs) == 1:
        RC = RCs[0]
        if RC[1] != X:
            return "IMPOSSIBLE"
        else:
            return "%.7f" % (float(V) / RC[0])
    elif len(RCs) == 2:
        RC1 = RCs[0]
        R1, C1 = RC1
        RC2 = RCs[1]
        R2, C2 = RC2
        ans = 10**100
        if C1 == X:
            ans = min(ans, float(V) / R1)
        if C2 == X:
            ans = min(ans, float(V) / R2)
        if C1 == C2 == X:
            ans = min(ans, V / (R1+R2))
        if C1 < X < C2 or C2 < X < C1:
            V1, V2 = cal_V(C1, C2, X, V)
            ans = min(ans, max(V1/R1, V2/R2))
        if ans == 10**100:
            return "IMPOSSIBLE"
        else:
            return ans
    else:
        return "IMPOSSIBLE"

def main():
    for T in range(1, 1+input()):
        N, V, X = read_array()
        N, V, X = int(N), float(V), float(X)
        RCs = []
        for _ in range(N):
            RCs.append(tuple(read_array(float))) # r, c
        ans = solve(RCs, V, X)
        print "Case #%d: %s" % (T, ans)
    pass



main()
