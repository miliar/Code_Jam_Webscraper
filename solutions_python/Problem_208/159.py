#! python3

import sys
from collections import deque

DATA_FILE = "C-small-attempt0"

def main():
    with open(DATA_FILE + ".in") as in_file:
        with open(DATA_FILE + ".out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '')
                N, Q = [int(n) for n in line.split()]
                horses = {}
                for i in range(1, N + 1):
                    line = in_file.readline().replace('\n', '')
                    E, S = [int(n) for n in line.split()]
                    horses[i] = E, S
                distances = {c: {} for c in range(1, N + 1)}
                for i in range(1, N + 1):
                    line = in_file.readline().replace('\n', '')
                    d = [int(n) for n in line.split()]
                    for j, dist in enumerate(d):
                        if dist != -1:
                            distances[i][j + 1] = dist
                deliveries = []
                for i in range(Q):
                    line = in_file.readline().replace('\n', '')
                    U, V = [int(n) for n in line.split()]
                    deliveries.append((U, V))

                connectivity_time = {c: {c: 0} for c in range(1, N + 1)}
                for c in range(1, N + 1):
                    q = deque()
                    speed = horses[c][1]
                    q.append((c, horses[c][0]))
                    while len(q) > 0:
                        node, dist_left = q.popleft()
                        for n in distances[node]:
                            dist = distances[node][n]
                            if dist <= dist_left:
                                current_best_time = connectivity_time[c].get(n, sys.maxsize)
                                new_time = connectivity_time[c][node] + distances[node][n] / speed
                                if new_time < current_best_time:
                                    connectivity_time[c][n] = new_time
                                q.append((n, dist_left - dist))

                for c in connectivity_time:
                    connectivity_time[c].pop(c)


                answers = []
                for u, v in deliveries:
                    dijk = {c: sys.maxsize for c in range(1, N + 1)}
                    dijk[u] = 0
                    visited = set()
                    while v not in visited:
                        curr = 0
                        min_city_dist = sys.maxsize
                        for city, dist in dijk.items():
                            if city not in visited:
                                if dist < min_city_dist:
                                    curr = city
                                    min_city_dist = dist
                        for n, dist in connectivity_time[curr].items():
                            new_dist = dijk[curr] + dist
                            if new_dist < dijk[n]:
                                dijk[n] = new_dist
                        visited.add(curr)
                    answers.append(dijk[v])

                fout.write("Case #{0}: {1}\n".format(x + 1, ' '.join([str(n) for n in answers])))

if __name__ == "__main__":
    main()
