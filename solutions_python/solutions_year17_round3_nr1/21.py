#!/usr/bin/python

import sys
import time
import itertools
import math

DEBUG = False


def read_test_data():
    N, K = readline([int, int])
    pancakes = []
    for _ in range(N):
        pancakes.append(readline([int, int]))  # radius, height

    return pancakes, K

def total_surface_area(pancakes, radius, K):
    first = None
    for i in range(len(pancakes)):
        if pancakes[i][0] == radius:
            first = i
            break

    sides = [2*math.pi*pancake[0]*pancake[1] for pancake in pancakes[first + 1:]]
    if len(sides) < K - 1:
        return 0
    sides.sort(reverse=True)
    total_sides = sum(sides[:K-1])

    # print "r:{} t:{} a:{}".format(radius, total_sides, math.pi * radius**2 + total_sides)

    return math.pi * radius**2 + total_sides + 2*math.pi*pancakes[first][0]*pancakes[first][1]


def compute_test_result(test_data):
    pancakes, K = test_data
    pancakes.sort(reverse=True)

    radii = set(pancake[0] for pancake in pancakes)
    return max(total_surface_area(pancakes, r, K) for r in radii)


def main():
    T = int(sys.stdin.readline())
    for i in range(1, T + 1):
        test_data = read_test_data()

        if DEBUG:
            start_time = time.time()
            print "Case #{} INPUT: {}".format(i, test_data)
            print "Case #{}: {}".format(i, compute_test_result(test_data))
            elapsed = time.time() - start_time
            print "TIME: {:.2f}s".format(elapsed)
            print
        else:
            print "Case #{}: {}".format(i, compute_test_result(test_data))


def readline(types):
    objects = []
    type_index = 0

    for token in sys.stdin.readline().split():
        objects.append(types[type_index](token))

        if type_index + 1 < len(types):
            type_index += 1

    return objects


def split_list(raw_list, index):
    return raw_list[:index] + [raw_list[index:]]


def find_augmenting_path_bfs(capacities, source, sink):
    assert source != sink

    parents = [None] * len(capacities)
    flow = [None] * len(capacities)

    parents[source], flow[source] = -2, float("inf")

    queue = [source]
    while queue:
        node = queue.pop()

        if node == sink:
            # flow found!
            path = []

    return None

def interval_queue(intervals):
    """
    Takes in a list of closed interval tuples: (a, b, data) corresponds to [a, b], marked with data.
    For each event, yields a set of the currently active intervals.
    """

    START_FLAG = 0
    END_FLAG = 1

    interval_events = []
    for interval in intervals:
        interval_events.append((interval[0], START_FLAG, interval))
        interval_events.append((interval[1], END_FLAG, interval))
    interval_events.sort()

    active_intervals = []
    yield active_intervals

    for interval_event in interval_events:
        event_type = interval_event[1]
        assert event_type in [START_FLAG, END_FLAG]
        if event_type == START_FLAG:
            active_intervals.append(interval_event[2])
        else:
            active_intervals.remove(interval_event[2])

        yield active_intervals


def floyd_warshall(adjacency):
    """
    Input: adjacency is a square matrix, where float("inf") denotes no path exists.
    Modifies in place.
    """
    nodes = len(adjacency)
    assert len(adjacency[0]) == nodes

    for t in range(nodes):
        for u, v in itertools.product(range(nodes), repeat=2):
            new_dist = adjacency[u][t] + adjacency[t][v]
            if new_dist < adjacency[u][v]:
                adjacency[u][v] = new_dist

if __name__ == "__main__":
    main()
