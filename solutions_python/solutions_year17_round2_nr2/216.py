from queue import PriorityQueue as PQ
T = int(input())
for t in range(1, T+1):
    n, r, o, y, g, b, v = map(int, input().split())
    if r*2 > n or y*2 > n or b*2 > n:
        print("Case #%d: IMPOSSIBLE" % t)
        continue
    lst = -1
    pq = PQ()
    if r > 0:
        pq.put((-r, 0))
    if y > 0:
        pq.put((-y, 1))
    if b > 0:
        pq.put((-b, 2))
    s = ""
    colors = {0: 'R', 1: 'Y', 2: 'B'}
    while not pq.empty():
        v, c = pq.get()
        if c == lst:
            v2, c2 = pq.get()
            s += colors[c2]
            v2 += 1
            if lst == -1:
                colors[-100] = colors[c2]
                c2 = -100
            if v2 < 0:
                pq.put((v2, c2))
            pq.put((v,c))
            lst = c2
            
        else:
            s += colors[c]
            v += 1
            if lst == -1:
                colors[-100] = colors[c]
                c = -100
            if v < 0:
                pq.put((v, c))
            lst = c
    d = {'R': 0, 'B': 0, 'Y': 0}
    lst = ''
    for c in s:
        d[c] += 1
        lst = c
    if len(s) != n:
        print("R should be %d but is %d" %(r, d['R']))
        print("B should be %d but is %d" %(b, d['B']))
        print("Y should be %d but is %d" %(y, d['Y']))
    assert(d['R'] == r)
    assert(d['B'] == b)
    assert(d['Y'] == y)
    assert(s[0] != s[-1])
    print("Case #%d: %s" % (t, s))
              
