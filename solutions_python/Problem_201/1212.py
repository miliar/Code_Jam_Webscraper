from queue import PriorityQueue

T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())

    p = PriorityQueue()
    p.put(-N)

    for j in range(K-1):
        spot = -p.get()
        l = spot - spot//2 - 1
        r = spot//2

        p.put(-l)
        p.put(-r)

    spot = -p.get()
    l = spot - spot//2 - 1
    r = spot//2

    print("Case #%d: %d %d" % (i, r, l))
