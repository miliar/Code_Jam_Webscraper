import sys
T = int(input())
for case in range(1, T+1):
    n, q = map(int, input().split())
    horses = []
    graph = []
    points = []
    for i in range(n):
        horses.append(list(map(int, input().split())))
    for i in range(n):
        graph.append(list(map(int, input().split())))
    for i in range(q):
        s, e = map(int, input().split())
        memo = dict()

        def solve(pos, dist, speed):
            if pos == e-1:
                return 0
            if (pos, dist, speed) in memo:
                return memo[(pos, dist, speed)]
            res = float("inf")
            d = graph[pos][pos+1]
            if dist >= d:
                res = d/speed + solve(pos+1, dist-d, speed)
            if horses[pos][0] >= d:
                res = min(res, d/horses[pos][1] + solve(pos+1, horses[pos][0]-d, horses[pos][1]))
            memo[(pos, dist, speed)] = res
            return res
        res = (solve(s-1, *horses[s-1]))
        print(f"Case #{case}: {res:.10f}")
