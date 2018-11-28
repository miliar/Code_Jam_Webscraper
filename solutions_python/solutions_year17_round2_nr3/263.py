# Zolmeister

# from collections import deque
from Queue import PriorityQueue

T = int(raw_input())

for t in xrange(T):
    N, Q = map(int, raw_input().split())
    horses = []
    for x in xrange(N):
        horses.append(map(int, raw_input().split()))
    graph = []
    for x in xrange(N):
        graph.append(map(int, raw_input().split()))

    deliveries = []
    for x in xrange(Q):
        deliveries.append(map(int, raw_input().split()))

    simple = []
    for i in xrange(N):
        simple.append([max(graph[i]), horses[i]])

    # print simple

    queue = PriorityQueue()
    queue.put([0.0, 0, simple[0][0], simple[0][1]])

    ans = 0
    seen = set()
    while not queue.empty():
        time, city, next_city_dist, horse = queue.get()
        if (city, tuple(horse)) in seen:
            continue
        seen.add((city, tuple(horse)))
        # print 'at city', city, 'with horse', horse

        if city == N - 1:
            ans = time
            break

        time += next_city_dist / float(horse[1])
        city += 1
        horse = [horse[0] - next_city_dist, horse[1]]

        if horse[0] < 0:
            continue

        queue.put([time, city, simple[city][0], horse])
        queue.put([time, city, simple[city][0], simple[city][1]])


    print 'Case #{}: {}'.format(t + 1, ans)
