import sys

f = open("B-large.in", "r")
T = int(f.readline())
for X in range(T):
    line = f.readline().strip().split()
    N = int(line.pop(0))
    S = int(line.pop(0))
    p = int(line.pop(0))
    t = []
    Y = 0
    while line != []:
        t.append(int(line.pop(0)))
    i = 0
    while i < len(t):
        if t[i]%3 == 0:
            if t[i]/3 >= p:
                Y += 1
                t.pop(i)
                i -= 1
        elif t[i]/3 >= p-1:
            Y += 1
            t.pop(i)
            i -= 1
        i += 1
    i = 0
    while i < len(t) and S != 0:
        if (p*3 - t[i]) <= 4 and t[i] != 0:
            Y += 1
            t.pop(i)
            i -= 1
            S -= 1
        i += 1
    print "Case #%d: %d" % (X+1, Y)