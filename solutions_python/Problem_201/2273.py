from queue import PriorityQueue as pq
T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    p = pq()
    p.put(-n)
    for i in range(k-1):
        r = -p.get()
        p.put(-(r//2))
        p.put(-((r-1)//2))
    r = -p.get()
    hi = r//2
    lo = (r-1)//2
    print("Case #%d: %d %d" % (t, hi,lo))
