#!/usr/bin/env python

fin = open("2.in", "r")
fout = open("2.out", "w")

def maken(l):
    return int(''.join(l))

T = int(fin.readline())
for t in range(T):
    print t+1
    N = list(fin.readline().strip())

    ans = []
    done = False
    for i in range(len(N)):
        ans.append('0')
        if done:
            ans[i] = '9'
            continue
        for j in range(10):
            if maken([str(j)] * (len(N)-i)) <= maken(N[i:]):
                ans[i] = str(j)
        if ans != N[:i+1]:
            done = True

    fout.write("Case #" + str(t+1) + ": " + str(maken(ans)) + "\n")
