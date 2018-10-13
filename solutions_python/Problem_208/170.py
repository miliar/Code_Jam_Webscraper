import sys
assert sys.version_info >= (3, 5)


def solve(prefix):
    N, Q = [int(_) for _ in input().split()]
    E = [None for _ in range(N)]
    S = [None for _ in range(N)]
    for i in range(N):
        E[i], S[i] = [int(_) for _ in input().split()]
    D = [None for _ in range(N-1)]
    for i in range(N):
        Di = [int(_) for _ in input().split()]
        if i < N-1:
            assert Di[i+1] != -1
            D[i] = Di[i+1]
    assert Q == 1
    u, v = [int(_) for _ in input().split()]
    assert u == 1 and v == N

    states = [(E[0], S[0], 0)]
    for i in range(N-1):
        ns = []
        for ce, cs, ans in states:
            ce -= D[i]
            ans += D[i]/cs
            if i == N-2:
                ns.append((ce, cs, ans))
                continue
            if ce < D[i+1]:
                if E[i+1] < D[i+1]:
                    continue  # dead state
                ns.append((E[i+1], S[i+1], ans))
            else:
                if S[i+1] >= cs:
                    if E[i+1] >= ce:
                        ns.append((E[i+1], S[i+1], ans))
                    else:
                        ns.append((E[i+1], S[i+1], ans))
                        ns.append((ce, cs, ans))
                else:
                    if E[i+1] >= ce:
                        ns.append((E[i+1], S[i+1], ans))
                        ns.append((ce, cs, ans))
                    else:
                        ns.append((ce, cs, ans))
        nns = []
        for i, (ce, cs, ans) in enumerate(ns):
            ok = True
            for j, (ce2, cs2, ans2) in enumerate(ns):
                if i == j:
                    continue
                if ce2 >= ce and cs2 >= cs and ans2 <= ans:
                    ok = False
                    break
            if ok:
                nns.append((ce, cs, ans))
        states = nns
    ans = None
    for ce, cs, ansX in states:
        if ans is None or ansX < ans:
            ans = ansX
    print('{}{:.7f}'.format(prefix, ans))


def main():
    T = int(input())
    for t in range(T):
        solve(prefix='Case #{}: '.format(t+1))


if __name__ == '__main__':
    main()
