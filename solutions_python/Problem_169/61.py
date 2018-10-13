def solve(N, V, X, R, C):
    if N==1:
        if X==C[0]:
            return "%.10f"%(V/R[0])
        else:
            return "IMPOSSIBLE"
    elif N==2:
        if min(C) <= X <= max(C):
            if abs(C[1]-C[0]) > 0.:
                v = V * abs(X-C[1]) / abs(C[1]-C[0])
                return "%.10f" % max(v/R[0], (V-v)/R[1])
            else:
                return "%.10f" % (V/sum(R))
        else:
            return "IMPOSSIBLE"
    else:
        return "???"

for t in range(input()):
    N,V,X = map(float, raw_input().split())
    N = int(N)
    R = [0.]*N
    C = [0.]*N
    for i in range(N):
        R[i],C[i] = map(float, raw_input().split())
    print "Case #%s: %s" % (t+1, solve(N,V,X,R,C))
