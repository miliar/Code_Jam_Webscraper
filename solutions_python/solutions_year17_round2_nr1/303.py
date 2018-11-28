#!/usr/bin/env python

fin = open("1.in", "r")
fout = open("1.out", "w")

T = int(fin.readline())
for t in range(T):
    print str(t+1)
    D, N = map(int, fin.readline().split())
    end_time = []
    for i in range(N):
        k, s = map(float, fin.readline().split())
        end_time.append((D - k) / s)

    time = max(end_time)
    ans = D / time
    fout.write("Case #" + str(t+1) + ": " + "{0:.6f}".format(ans) + "\n")
