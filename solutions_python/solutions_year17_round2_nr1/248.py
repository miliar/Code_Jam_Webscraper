import sys

data = sys.stdin.readlines()
t = int(data[0])
l = 1
for i in range(t):
    print "Case #%d:" % (i+1),

    d = data[l].split()
    l += 1

    D = float(d[0])
    N = int(d[1])
    T = 0

    for j in range(N):
        d = data[l].split()
        l += 1

        k_i = float(d[0])
        s_i = float(d[1])

        t_i = (D - k_i) / s_i
        if t_i > T:
            T = t_i

    s = D/T

    print "%.6f" % s
