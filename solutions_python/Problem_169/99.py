from sys import stdin, stdout

EPS = 1E-6

def solve(V, X, taps):
    # RATE taps[0]
    # TEMP taps[1]

    taps.sort(key=lambda i:i[1])

    if X < (taps[0][1] - EPS) or X > (taps[-1][1] + EPS):
        return "IMPOSSIBLE"


    #(V0X0 + V1X1) / (V0 + V1)    
    # 2 tap case
    #if len(taps) > 2:
    #    raise RuntimeError

    if (len(taps) == 1) or (len(taps) == 2 and (taps[1][1] - taps[0][1]) < EPS):
        rate = sum(t[0] for t in taps)

        return "%.9f"%(V / rate)

    V1 = (V * (X - taps[0][1])) / (taps[1][1] - taps[0][1])
    V0 = V - V1

    return "%.9f"%max(V1/taps[1][0], V0/taps[0][0])



if __name__ == '__main__':

    T = int(stdin.readline())

    for i in range(T):
        # read input for this problem

        inp = stdin.readline().strip().split()
        N = int(inp[0])
        V = float(inp[1])
        X = float(inp[2])

        taps = []
        for j in range(N):
            taps.append(map(float, stdin.readline().strip().split()))

        result = solve(V, X, taps)

        print "Case #%d: %s"%(i+1, result)