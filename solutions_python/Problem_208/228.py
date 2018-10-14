from Queue import PriorityQueue

fin = open('C-small-attempt0.in')
fout = open('output.txt', 'w')
T = int(fin.readline())
for tt in range(T):
    N, Q = map(int, fin.readline().split(' '))
    horse = {}
    for i in range(N):
        E, S = map(int, fin.readline().split(' '))
        horse[i] = (E, S)
    edges = {}
    dist = [0]
    for i in range(N - 1):
        es = map(int, fin.readline().split(' '))
        dist.append(dist[-1] + es[i + 1])
    fin.readline()
    U, V = map(int, fin.readline().split(' '))
    for i in range(N - 1):
        for j in range(i + 1, N):
            if horse[i][0] >= dist[j] - dist[i]:
                edges.setdefault(i, [])
                edges[i].append((j, float(dist[j] - dist[i]) / horse[i][1]))

    pq = PriorityQueue()
    pq.put((0, 0))
    path = [float('inf')] * N
    path[0] = 0

    while not pq.empty():
        dist, u = pq.get()
        if u == N - 1:
            fout.write("Case #%s: %s\n" % (tt + 1, dist))
            break
        for v, di in edges[u]:
            if path[v] > path[u] + di:
                path[v] = path[u] + di
                pq.put((path[v], v))

fin.close()
fout.close()