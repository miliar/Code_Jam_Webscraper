import sys

def solve(S, K):
    flips = 0
    while len(S) >= K:
        if not S[-1]:
            S[-K:] = [not sc for sc in S[-K:]]
            flips += 1
        del S[-1]
    return flips if all(S) else 'IMPOSSIBLE'

if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        S, K = sys.stdin.readline().split()
        S = [sc == '+' for sc in S]
        K = int(K)
        assert 2 <= K <= len(S)
        print "Case #%d: %s" % (i+1, solve(S, K))
