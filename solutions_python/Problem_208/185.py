__author__ = 'Tom'

with open ('C-small-attempt0.in', 'r') as f:
    with open ('q3solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            line1 = f.readline().split()
            N = int(line1[0])
            Q = int(line1[1])
            horses = []
            for i in range(N):
                line2 = f.readline().split()
                ei = int(line2[0])
                si = int(line2[1])
                horses.append((ei, si))

            graph = []
            for i in range(N):
                line3 = f.readline().split()
                graph.append([int(x) for x in line3])

            city_line = [graph[i][i+1] for i in range(N-1)]
            distances = []

            for i in range(Q):
                line4 = f.readline().split()
                c_start = int(line4[0]) - 1
                c_end = int(line4[1]) - 1
                avail = []  # list of (time, dist_remain, speed)
                avail.append([0, horses[c_start][0], horses[c_start][1]])
                for j in range(c_start, c_end):
                    min_time = None
                    to_remove = []
                    for h_i in range(len(avail)):
                        h = avail[h_i]
                        if h[1] < city_line[j]:
                            if not min_time:
                                min_time = h[0]
                            elif h[0] < min_time:
                                min_time = h[0]
                            to_remove.append(h_i)

                    new_avail = []
                    for i in range(len(avail)):
                        if i not in to_remove:
                            new_avail.append(avail[i])
                    avail = new_avail
                    # add switch horses
                    new = []
                    for h_i in range(len(avail)):
                        h = avail[h_i]
                        new.append([h[0],horses[j][0], horses[j][1]])
                    avail.extend(new)
                    if min_time:
                        avail.append([min_time, horses[j][0], horses[j][1]])
                    # move
                    for h_i in range(len(avail)):
                        h = avail[h_i]
                        h[1] -= city_line[j]
                        h[0] += city_line[j] / h[2]

                final_times = [h[0] for h in avail]
                distances.append(min(final_times))
            ans = " ".join([str(x) for x in distances])

            solution.write('Case #' + str(case+1) + ': ' + ans + '\n')
