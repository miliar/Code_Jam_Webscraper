from queue import PriorityQueue

with open("bathroom.in", "r") as f:
    cases = int(f.readline())
    for case in range(1, cases+1):
        n, k = list(map(int, f.readline().split(" ")))
        y = z = n
        Q = PriorityQueue()
        Q.put((-n, n))
        for i in range(1, k+1):
            l = Q.get()[1]
            y = l//2
            z = l//2-1 if l%2 == 0 else l//2
            Q.put((-y, y))
            Q.put((-z, z))
        print("Case #%d: %d %d" % (case, y, z))
