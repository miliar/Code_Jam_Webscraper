__author__ = 'PrimuS'


f = open("d:\\dev\\acm\\codeJam 2015\\B-small-attempt1.in", "r")
of = open("d:\\dev\\acm\\codeJam 2015\\B-small-res.txt", "w")

T = int(f.readline())

for t in range(1, T + 1):
    s = f.readline().split()
    n = int(s[0])
    v = float(s[1])
    x = float(s[2])
    r = [0] * n
    c = [0] * n
    for i in range(n):
        r[i], c[i] = [float(p) for p in f.readline().split()]

    print("Case #{:d}: ".format(t), end='', file=of)
    if n == 1:
        if c[0] != x:
            print("IMPOSSIBLE", file=of)
        else:
            print("{:.10f}".format(v / r[0]), file=of)
    elif n == 2:
        if c[0] > c[1]:
            c[0], c[1] = c[1], c[0]
            r[0], r[1] = r[1], r[0]

        if c[0] == c[1]:
            if c[0] != x:
                print("IMPOSSIBLE", file=of)
            else:
                print("{:.10f}".format(v / (r[0] + r[1])), file=of)
        elif c[0] == x:
            print("{:.10f}".format(v / r[0]), file=of)
        elif c[1] == x:
            print("{:.10f}".format(v / r[1]), file=of)
        elif x < c[0] or x > c[1]:
            print("IMPOSSIBLE", file=of)
        else:
            t2 = (x * v - c[0] * v) / (r[1] * c[1] - r[1] * c[0])
            t1 = (v - r[1] * t2) / r[0]
            if t1 < 0:
                print("IMPOSSIBLE", file=of)
            else:
                print("{:.10f}".format(max(t1, t2)), file=of)
    else:
        print("WTF ? " + t)

of.close()