import sys
from bisect import bisect_right
import itertools


def read_weights():
    return [
        num[2:]
        for num in sys.stdin.readline().strip().split()
    ]


def war(naomi, ken):
    naomi_pts = 0
    for n in naomi:
        kens_move = bisect_right(ken, n)
        if kens_move != len(ken):
            del ken[kens_move]
        else:
            naomi_pts += 1
            # Ken plays the smallest value he has
            del ken[0]

    return naomi_pts

def get_path(graph, start, end, path):
    if start == end:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = get_path(graph, neighbor, end, path + [neighbor])
            if new_path is not None:
                return new_path


def max_flow(graph):
    flow = 0
    while True:
        path = get_path(graph, 'source', 'sink', ['source'])
        if path is None:
            break
        fast_iter = iter(path)
        fast_iter.next()
        for e1, e2 in zip(path, fast_iter):
            graph[e1].remove(e2)
            graph[e2].append(e1)
        flow += 1

    return flow

def deceitful_war(naomi, ken):
    graph = {}
    for n, k in itertools.product(naomi, ken):
        if n > k:
            if n not in graph:
                graph[n] = []
            graph[n].append(k)

    graph['source'] = []
    for n in naomi:
        graph['source'].append(n)
        if n not in graph:
            graph[n] = []

    for k in ken:
        if k not in graph:
            graph[k] = []
        graph[k].append('sink')
    graph['sink'] = []


    return max_flow(graph)


def solve():
    # discard this line...
    sys.stdin.readline()
    naomi = read_weights()
    ken = read_weights()

    naomi.sort()
    ken.sort()

    war_result = war(list(naomi), list(ken))
    deceitful_war_result = deceitful_war(list(naomi), list(ken))

    return deceitful_war_result, war_result


def main():
    T = int(sys.stdin.readline().strip())
    for test in xrange(T):
        deceit, fair = solve()
        print 'Case #{0}: {1} {2}'.format(test + 1, deceit, fair)


if __name__ == '__main__':
    main()
