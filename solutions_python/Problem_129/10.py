#!/usr/bin/python3

from common import *

mod = 1000002013

def gain(k):
    return (k * (k + 1)) // 2

# We number the stations from 0 to (n - 1)
def testcase(x):
    n, m = readintegers()
    o = [0] * m
    e = [0] * m
    p = [0] * m
    for i in range(m):
        o[i], e[i], p[i] = readintegers()

    normal = 0
    for i in range(m):
        normal += gain(e[i] - o[i]) * p[i]

    origins = {}
    ends = {}
    for i in range(m):
        if o[i] in origins:
            origins[o[i]].append(i)
        else:
            origins[o[i]] = [i]
        if e[i] in ends:
            ends[e[i]].append(i)
        else:
            ends[e[i]] = [i]

    stations = list(origins.keys()) + list(ends.keys())
    stations.sort()
    rev_stations = stations[:]
    rev_stations.reverse()

    count = {}
    for station in stations:
        count[station] = 0

    optimal = 0
    last_station = -1
    for station in stations:
        if station == last_station:
            continue
        last_station = station

        # People boarding
        for j in origins.get(station, []):
            count[station] += p[j]

        # People leaving
        num_leaving = 0
        for j in ends.get(station, []):
            num_leaving += p[j]

        for j in rev_stations:
            if num_leaving == 0:
                break
            if count[j] == 0:
                continue
            k = min(count[j], num_leaving)
            optimal += k * gain(station - j)
            count[j] -= k
            num_leaving -= k

    score = (optimal - normal) % mod
    # print (x, n, m, optimal, normal, score)

    writeline("Case #%d: %d" % (x, score))

run_tests(testcase)
