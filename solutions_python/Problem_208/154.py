import StringIO

import networkx

from ecodejam.input_parser import read_int, set_parsed_input, run_solver, next_line


def solve_small(case_index):
    n = read_int()
    q = read_int()
    next_line()

    print "N:", n
    assert q == 1

    e = []
    s = []

    for i in xrange(n):
        e.append(float(read_int()))
        s.append(float(read_int()))
        next_line()

    d = []

    for i in xrange(n):
        cur = []
        for j in xrange(n):
            cur.append(float(read_int()))
        next_line()
        d.append(cur)

    u = []
    v = []

    for i in xrange(q):
        u.append(read_int())
        v.append(read_int())
        next_line()

    assert u[0] == 1, v[0] == n

    g = networkx.DiGraph()

    for i in xrange(1, n + 1):
        g.add_node(i)

    for i in xrange(1, n):
        horse_kms = e[i - 1]
        horse_speed = s[i - 1]

        j = i
        traveled = 0
        while j < n:
            dist_to_next_city = d[j - 1][j]
            print "Dist to next", dist_to_next_city
            traveled += dist_to_next_city
            horse_kms -= dist_to_next_city

            if horse_kms < 0:
                break
            j += 1
            g.add_edge(i, j, {"time": traveled / horse_speed})


    print g.edge
    path_length = networkx.shortest_path_length(g, 1, n, "time")
    # path_length = 0

    return "{:.6f}".format(path_length)


solve = solve_small

SAMPLE = """
2
3 1
2 3
2 4
4 4
-1 1 -1
-1 -1 1
-1 -1 -1
1 3
4 1
13 10
1 1000
10 8
5 5
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 10
-1 -1 -1 -1
1 4
4 3
30 60
10 1000
12 5
20 1
-1 10 -1 31
10 -1 10 -1
-1 -1 -1 10
15 6 -1 -1
2 4
3 1
3 2
"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
