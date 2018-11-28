import sys



if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for t in range(1, T+1):
        N, K = sys.stdin.readline().strip().split()
        N = int(N)
        U = float(sys.stdin.readline().strip())
        P = sorted(float(x) for x in sys.stdin.readline().strip().split())
        P.append(1.0)

        pp = P[0]
        for i in range(1, len(P)):
            if U > (P[i] - pp) * i:
                U -= (P[i] - pp) * i
                pp = P[i]
                for j in range(i):
                    P[j] = pp
            else:
                up = U / i
                for j in range(i):
                    P[j] += up
                break
        del P[-1]
        S = 1.0
        for p in P:
            S *= p



        print("Case #%s: %s" % (t, S))
