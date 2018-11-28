adjlist = []
for i in range(1000005):
    j = int(str(i)[::-1])
    adjlist.append((i+1, j))

for tc in range(1, int(raw_input())+1):
    n = int(raw_input())
    visited = [False] * 1000005
    visited[1] = True
    dist = [-1] * 1000005
    dist[1] = 1
    queue = [1]
    size = 1
    found = False
    while not found:
        u = queue.pop(0)
        size -= 1
        if u == n:
            found = True
        else:
            for v in adjlist[u]:
                if visited[v] == False:
                    visited[v] = True
                    dist[v] = dist[u]+1
                    queue.append(v)
                    size += 1
    print 'Case #%d: %d' % (tc, dist[n])