#!/usr/bin/env python

fin = open("3.in", "r")
fout = open("3.out", "w")

T = int(fin.readline())
for t in range(T):
    print str(t+1)
    N, Q = map(int, fin.readline().split())
    E = []
    S = []
    for i in range(N):
        e, s = map(float, fin.readline().split())
        E.append(e)
        S.append(s)
    D = []
    for i in range(N):
        D.append(map(float, fin.readline().split()))
    # cities are in a line
    dist = [D[i][i+1] for i in range(N-1)]
    # only query is 0, N-1
    fin.readline()

    # time[i][j][0] is how long you need to get to the ith city if you're on the horse from the j-th one at the end
    # time[i][j][1] is how much range you have on the current horse if you're on the jth horse at ith city
    time = [[[0.0, 0.0] for i in range(N)] for j in range(N)]
    time[0][0][1] = float(E[0])
    for i in range(1, N):
        for j in range(i):
            if time[i-1][j][0] == -1 or time[i-1][j][1] < dist[i-1]:
                time[i][j][0] = -1
                continue
            time[i][j][0] = time[i-1][j][0] + (dist[i-1] / S[j])
            time[i][j][1] = time[i-1][j][1] - dist[i-1]
        time[i][i][0] = min([time[i][j][0] for j in range(i) if time[i][j][0] != -1])
        time[i][i][1] = float(E[i])

    ans = time[N-1][N-1][0]
    fout.write("Case #" + str(t+1) + ": " + "{0:0.6f}".format(ans) + "\n")
