import logging
import Queue as Q
import math
import pprint

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def compute(N, Q, horses, distance_grid, U, V):
    # print N
    # print horses
    # for r in distance_grid:
    #     print r
    # print U,V

    list_of_horses = dict()
    for i in xrange(len(horses)):
        list_of_horses[i] = [[i,horses[i]]]
    # print list_of_horses

    min_time_to_city = [dict() for _ in xrange(N)]
    queue = [U]
    min_time_to_city[U][U] = 0
    while queue:
        v = queue.pop(0)
        for i in xrange(len(distance_grid[v])):
            dist = distance_grid[v][i]
            if dist == -1:
                continue
            queue.append(i)
            minimum_time_to_i = 9999999999999999999999
            for h_index in xrange(len(list_of_horses[v])):
                h = list_of_horses[v][h_index]
                assert(len(h)==2)
                assert(len(h[1])==2)
                extra_dist = h[1][0]-dist
                if extra_dist >= 0:
                    if extra_dist > 0:
                        list_of_horses[i].append([h[0], [extra_dist, h[1][1]]])
                    time_to_i = dist*1.0/h[1][1]+min_time_to_city[v][h[0]]
                    if time_to_i < minimum_time_to_i:
                        minimum_time_to_i = time_to_i
                    if h[0] not in min_time_to_city[i]:
                        min_time_to_city[i][h[0]] = time_to_i
            min_time_to_city[i][i] = minimum_time_to_i

    # print "MINIMUM TIME TO V:"
    # print min_time_to_city
    minimum_time = 99999999999999999999
    for city_ind in min_time_to_city[V]:
        t = min_time_to_city[V][city_ind]
        # print t,city_ind
        if t < minimum_time:
            minimum_time = t
    return minimum_time

t = int(raw_input())
for i in xrange(1, t + 1):
    logging.info("Solving case: {}".format(i))

    N, Q = [int(x) for x in raw_input().split(" ")]
    horses = []
    for _ in xrange(N):
        # Each horse is a tuple (max_distance,constant speed)
        horses.append([int(x) for x in raw_input().split(" ")])
    distance_grid = [None for _ in xrange(N)]
    for j in xrange(N):
        distance_grid[j] = list([int(x) for x in raw_input().split(" ")])

    print "Case #{}:".format(i),
    for _ in xrange(Q):
        U, V = (int(x) for x in raw_input().split(" "))
        result = compute(N, Q, horses, distance_grid, U-1, V-1)
        # print "{:.7f}".format(result),
        print result,
    print ''
