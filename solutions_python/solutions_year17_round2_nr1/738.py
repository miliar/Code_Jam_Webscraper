
# from collections import defaultdict, deque, Counter, OrderedDict
# from orderedset import OrderedSet
# from heapq import *
# import numpy as np
# from numpy import *
# import networkx as nx

# def play_graph():
#     G = nx.DiGraph()
#     G.add_edge(1, 2, weight=1)
#     G.add_edge(2, 3, weight=4)
#     G.add_edge(1, 4, weight=3)
#     G.add_edge(4, 3, weight=1)
#
#     print nx.topological_sort(G)
#     print nx.shortest_path(G, source=1, target=3, weight='weight')


def solve_test(D, N, S, K):

    # print "D, N, S, K"
    # print D, N, S, K

    T = [ float(D - K[idx]) / S[idx] for idx in xrange(len(S))]

    # print T

    sol = max(S[0], D / T[0])

    for idx in xrange(len(S)):
        sol = min(sol, max(S[idx], D / T[idx]))

    # print sol

    return sol





def parse_input_simple(f, g):
    for idx, test in enumerate(f.readlines()[1:]):
        g.write("Case #{0}: {1}".format(idx, solve_test(test)))
        g.write("\n")


def parse_input_multiple_lines(f, g):

    lines     = f.readlines()
    num_tests = int(lines[0].strip())
    test      = 1
    idx       = 1

    while test <= num_tests:

        # parse input
        line = lines[idx].rstrip()

        D, N = map(float, line.split())
        s, k = [], []

        for jdx in xrange(int(N)):

            idx   += 1
            line   = lines[idx].rstrip()
            kj, sj = map(float, line.split())

            if kj == D:
                continue

            s.append(sj)
            k.append(kj)

        g.write("Case #{0}: {1:.6f}".format(test, solve_test(D, N, s, k)))
        g.write("\n")

        idx  += 1
        test += 1


def solve(file):

    with open(file, "r") as f:
        with open("res", "w") as g:
            parse_input_multiple_lines(f, g)


def main():
    # solve("{0}-small-attempt0.in".format(__file__[:-3]))
    solve("{0}-large.in".format(__file__[:-3]))


if __name__ == "__main__":
    main()