#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    N, Q = [int(x) for x in raw_input().split()]
    dist, speed, grid = [0]*N, [0]*N, [0]*N
    for i in xrange(N):
        dist[i], speed[i] = [int(x) for x in raw_input().split()]
    for i in xrange(N):
        grid[i] = [int(x) for x in raw_input().split()]
    start, end = [int(x) for x in raw_input().split()]
    start -= 1
    end -= 1

    min_time = [[] for _ in xrange(N)]
    min_dist = [[] for _ in xrange(N)]
    stack = [(0, dist[start], speed[start], start)]  # time, dist, speed, node
    while len(stack):
        current_time, current_dist, current_speed, current_node = stack.pop()
        if current_node == end:
            continue
        for next_node in xrange(N):
            if next_node == start:
                continue
            next_dist = grid[current_node][next_node]
            if next_dist > -1:
                if next_dist <= current_dist:
                    new_dist = current_dist - next_dist
                    next_time = current_time + next_dist/float(current_speed)
                    possible = True
                    for i in xrange(len(min_time[next_node])):
                        if min_time[next_node][i] <= next_time and min_dist[next_node][i] >= new_dist:
                            possible = False
                            break
                    if possible:
                        stack.append((next_time, current_dist-next_dist, current_speed, next_node))
                        min_time[next_node].append(next_time)
                        min_dist[next_node].append(new_dist)

                if (speed[current_node] > current_speed or dist[current_node] > current_dist) and next_dist <= dist[current_node]:
                    new_dist = dist[current_node] - next_dist
                    next_time = current_time + next_dist/float(speed[current_node])
                    possible = True
                    for i in xrange(len(min_time[next_node])):
                        if min_time[next_node][i] <= next_time and min_dist[next_node][i] >= new_dist:
                            possible = False
                            break
                    if possible:
                        stack.append((next_time, dist[current_node]-next_dist, speed[current_node], next_node))
                        min_time[next_node].append(next_time)
                        min_dist[next_node].append(new_dist)

    print min(min_time[end])
