from math import inf
t = int(input())

for tc in range(t):
    n, q = map(int, input().split())
    horses = []
    for _ in range(n):
        horses.append([int(x) for x in input().split()])
    dist = []
    for i in range(n):
        for j, d in enumerate(map(int, input().split())):
            if j == i+1:
                dist.append(d)
    dist.append(0)
    for _ in range(q):
        input()

    arrival = [inf for _ in range(n)]

    arrival[0] = 0

    for i, a in enumerate(arrival):
        time = a
        d = horses[i][0]
        s = horses[i][1]
        for j in range(i, n):
            if d<0:
                break
            arrival[j] = min(arrival[j], time)
            d -= dist[j]
            time += dist[j] / s

    print('Case #{}: {}'.format(str(tc+1), str(arrival[-1])))
