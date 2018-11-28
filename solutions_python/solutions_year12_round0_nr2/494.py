import numpy as np
def solve(n, surp):
    if n < 0:
        return 0
    if vals[n, surp] == -1:
        a = scores[n] / 3
        r = scores[n] % 3
        if a >= p:
            vals[n, surp] = solve(n-1, surp) + 1
        elif a < p-2:
            vals[n, surp] = solve(n-1, surp)
        elif r >= 1 and a == p - 1:
            vals[n, surp] = solve(n-1, surp) + 1
        elif r == 0 and a == p - 1:
            if surp > 0 and a > 0:
                vals[n, surp] = max(solve(n-1, surp-1) + 1, solve(n-1, surp))
            else:
                vals[n, surp] = solve(n-1, surp)
        elif r == 2 and a == p - 2:
            if surp > 0:
                 vals[n, surp] = max(solve(n-1, surp-1) + 1, solve(n-1, surp))
            else:
                vals[n, surp] = solve(n-1, surp)
        else:
            vals[n, surp] = solve(n-1, surp)
    return vals[n, surp]

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        scores = [int(s) for s in raw_input().split()]
        N = scores[0]
        S = scores[1]
        p = scores[2]
        scores = scores[3:]
        vals = []
        for j in range(N):
            vals.append([])
            for surp in range(S+1):
                vals[j].append(-1)
        vals = np.array(vals)
        print "Case #"+str(i)+": "+str(solve(N-1, S))
        #print vals
