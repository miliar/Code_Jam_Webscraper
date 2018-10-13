import sys



if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for t in range(1, T+1):
        D, N = sys.stdin.readline().strip().split()
        D = float(D)
        N = int(N)
        Ts = []
        for i in range(N):
            K, S = sys.stdin.readline().strip().split()
            Ts.append((D - float(K)) / float(S))
        S = D / max(Ts)
        print("Case #%s: %s" % (t, S))
