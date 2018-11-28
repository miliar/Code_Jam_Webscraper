import queue


T = int(input())


def solve(N, K):
    que = queue.PriorityQueue()
    a = N // 2
    b = N - 1 - a
    que.put((-a, -b))
    res = []
    while not que.empty():
        a, b = que.get()
        a = -a
        b = -b
        res.append((a, b))
        if a != 0:
            naa = a // 2
            nab = a - 1 - naa
            que.put((-naa, -nab))
        if b != 0:
            nba = b // 2
            nbb = b - 1 - nba
            que.put((-nba, -nbb))
    return res[K - 1]


for t in range(T):
    N, K = map(int, input().split())
    ans = solve(N, K)
    print("Case #{}: {} {}".format(t + 1, max(ans), min(ans)))
