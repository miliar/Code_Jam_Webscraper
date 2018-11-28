from sys import stdin

def solve(R, k, N, g):
    class Group: pass
    G = [Group() for i in range(N)]
    for i in range(N):
        G[i].size = g[i]
    for i in range(N):
        G[i].all = G[i].size
        j = (i + 1) % N
        G[i].to = j
        while G[i].all + G[j].size <= k and j != i:
            G[i].all += G[j].size
            j = (j + 1) % N
            G[i].to = j
    money = 0
    going = 0
    for r in range(R):
        money += G[going].all
        going  = G[going].to
    return money

T = int(stdin.readline())
for no in range(1, T + 1):
    R, k, N = map(int, stdin.readline().split())
    g = map(int, stdin.readline().split())
    answer = solve(R, k, N, g)
    print "Case #%s: %s" % (no, answer)
