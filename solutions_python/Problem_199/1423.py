import sys

def flip(ps, i, k):
    for m in range(i, i+k):
        ps[m] = not ps[m]

def min_flips(ps, K):
    S = len(ps)
    n = 0
    for i in range(0, S-K+1):
        if not ps[i]:
            flip(ps, i, K)
            n += 1

    for i in range(S-K+1, S):
        if not ps[i]:
            return "IMPOSSIBLE"
    return n




if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for t in range(1, T+1):
        ps, K = sys.stdin.readline().strip().split()
        K = int(K)
        ps = [p == "+" for p in ps]
        # print(ps)
        flips = min_flips(ps, K)
        print("Case #%s: %s" % (t, flips))
