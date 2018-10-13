import sys

(_stdin, sys.stdin) = (sys.stdin, open('D-small-attempt0.in', 'r'))
(_stdout, sys.stdout) = (sys.stdout, open('D-small.out', 'w'))

T = int(input())


def common(s, t):
    k = 0
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            return k
        k += 1
    return k


def get_nodes(S):
    ans = 1
    for i in range(len(S)):
        x = 0
        for j in range(i):
            x = max(x, common(S[i], S[j]))
        ans += len(S[i]) - x
    return ans


def dfs(SS, S, K, M, N, O):
    if K == M:
        if min([len(v) for v in SS]) > 0:
            #print(SS, sum([get_nodes(s) for s in SS]))
            cc = sum([get_nodes(s) for s in SS])
            O[cc] = O.get(cc, 0) + 1
        return
    for i in range(N):
        #print(SS, i, S, K)
        SS[i].append(S[K])
        dfs(SS, S, K+1, M, N, O)
        SS[i].pop()


for t in range(1, T+1):
    M, N = map(int, input().split())
    S = [input().strip() for m in range(M)]
    SS = [[] for x in range(N)]
    O = {}
    dfs(SS, S, 0, M, N, O)
    print('Case #%d: %d %d' % (t, max(O), O[max(O)]))