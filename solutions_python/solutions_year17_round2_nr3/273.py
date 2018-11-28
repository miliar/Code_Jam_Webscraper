INF = 10e9 + 1

T = int(raw_input())

for i in xrange(T):
    [N, Q] = map(int, raw_input().split())

    endurances = []
    speeds = []
    graph = []
    solution = [INF for j in xrange(N)]
    dist = [0]
    interests=  []

    for j in xrange(N):
        [e, s] = map(int, raw_input().split())
        endurances.append(e)
        speeds.append(float(s))

    for j in xrange(N):
        row = map(int, raw_input().split())
        graph.append(row)
        if (j != N - 1):
            dist.append(dist[-1] + row[j+1])

    for j in xrange(Q):
        [u, v] = map(lambda x: int(x) - 1, raw_input().split())
        interests.append((u, v))

    solution[N - 1] = 0

    solution[N - 2] = (dist[N - 1] - dist[N - 2]) / speeds[N - 2]

    for j in xrange(N - 3, -1, -1):
        if endurances[j] >= dist[j + 1] - dist[j]:
            solution[j] = (dist[j + 1] - dist[j]) / speeds[j] + solution[j+1] # change horse at next town

            k = j + 2

            while (k < N and endurances[j] >= dist[k] - dist[j]):
                solution[j] = min(((dist[k] - dist[j]) / speeds[j] + solution[k], solution[j]))
                k+=1;

    #print endurances
    #print speeds
    #print solution
    #print dist

    print "Case #%d: %f" % (i + 1, solution[0])
