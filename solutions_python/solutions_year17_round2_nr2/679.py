
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


def make_single_lane(N, T2, T1, S2, S1):

    if T1 == 0 and T2 == 0:
        return 0, None

    if T2 == 0:
        return T1, None

    if T1 == T2:
        if T1 + T2 == N:
            return 0, (S2 + S1) * T1
        else:
            return -1, None

    if T2 < T1:
        return -1, None

    return T2 - T1 - 1, (S2 + S1) * T1 + S2


def solve_test(test):

    N, R, O, Y, G, B, V = map(int, test.split())

    # print "TEST", test

    solutie = ""

    Y, Y_lane = make_single_lane(N, Y, V, "Y", "V")
    if Y == -1:
        return "IMPOSSIBLE"
    if Y_lane:
        solutie += Y_lane

    B, B_lane = make_single_lane(N, B, O, "B", "O")
    if B == -1:
        return "IMPOSSIBLE"
    if B_lane:
        solutie += B_lane

    R, R_lane = make_single_lane(N, R, G, "R", "G")
    # print R, R_lane
    if R == -1:
        return "IMPOSSIBLE"
    if R_lane:
        solutie += R_lane

    lant = [(Y, 'Y'), (B, 'B'), (R, 'R')]

    # print solutie

    idx      = -1
    last_idx = -1

    if solutie[-1] == 'Y':
        last_idx = 0
    elif solutie[-1] == 'B':
        last_idx = 1
    elif solutie[-1] == 'R':
        last_idx = 2

    rem_symb = None
    rem_count = 0

    tests = 0
    while len(solutie) < N:

        # print lant, solutie, idx
        idx += 1
        if idx == 3:
            idx = 0
        # print idx

        count, symb = lant[idx]

        if count == 0:
            continue

        if idx == last_idx:
            rem_idx, rem_symb, rem_count = last_idx, symb, count
            break

        count   -= 1
        solutie += symb
        lant[idx] = (count, symb)

        last_idx = idx
        # idx      += 1

    sanity_check = {
        "Y": {"R", "B"},
        "R": {"Y", "B"},
        "B": {"Y", "R"}
    }

    print "OVEEER", rem_symb, solutie

    if rem_symb:

        valid = sanity_check[rem_symb]

        idx = 0

        while idx < len(solutie) - 1 and rem_count > 0:

            cpos = idx
            npos = idx + 1

            # print solutie[cpos], solutie[npos]

            if solutie[cpos] in valid and solutie[npos] in valid:
                solutie = solutie[:cpos + 1] + rem_symb + solutie[npos:]
                idx += 2
                rem_count -= 1
            else:
                idx += 1

    if len(solutie) != N:
        return "IMPOSSIBLE"

    # print "OVER", solutie, rem_count

    if solutie[0] == solutie[-1] or solutie[-1] == solutie[-2]:

        rem_symb  = solutie[-1]
        solutie   = solutie[:-1]
        rem_count = 1

        valid = sanity_check[rem_symb]
        idx   = 0

        while idx < len(solutie) - 1 and rem_count > 0:

            cpos = idx
            npos = idx + 1

            # print solutie[cpos], solutie[npos]

            if solutie[cpos] in valid and solutie[npos] in valid:
                # print "scoti cheia"
                solutie = solutie[:cpos + 1] + rem_symb + solutie[npos:]
                # print solutie
                idx += 2
                rem_count -= 1
            else:
                idx += 1

        if rem_count > 0:
            return "IMPOSSIBLE"

        # solutie = solutie[:-2] + solutie[-1] + solutie[-2]

    # if solutie[-1] == solutie[-2]:
    #     solutie = solutie[-1] + solutie[1:] + solutie[0]

    if solutie[0] == solutie[-1] or solutie[0] == solutie[-1]:
        return "IMPOSSIBLE"

    # print "OVER", solutie

    check = [("Y", {"R", "B", "V"}), ("R", {"Y", "B", "G"}), ("B", {"Y", "R", "O"}),
             ("V", {"Y"}), ("O", {"B"}), ("G", {"R"})]

    print len(solutie), solutie, solutie[0], solutie[-1]

    for col, perm in check:

        if solutie[-1] == col:
            if solutie[-2] not in perm or solutie[0] not in perm:
                return "IMPOSSIBLE"

        if solutie[-2] == col:
            if solutie[-3] not in perm or solutie[-1] not in perm:
                return "IMPOSSIBLE"

    # print Y_lane, B_lane, R_lane
    # print solutie

    return solutie


def parse_input_simple(f, g):
    for idx, test in enumerate(f.readlines()[1:]):
        g.write("Case #{0}: {1}".format(idx + 1, solve_test(test)))
        g.write("\n")
        # exit(0)


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
            parse_input_simple(f, g)


def main():
    # solve("{0}-small.in".format(__file__[:-3]))
    solve("{0}-small-attempt2.in".format(__file__[:-3]))
    # solve("{0}-large.in".format(__file__[:-3]))


if __name__ == "__main__":
    main()