fin = open("a.in")
fout = open("a.out", "w")

nt = int(fin.readline())

for tn in xrange(nt):
    fout.write("Case #" + str(tn + 1) + ": ")

    d, n = (int(i) for i in fin.readline().split())
    mt = 0.
    for i in range(n):
        a, b = (int(c) for c in fin.readline().split())
        ct = 1. * (d - a) / b
        if mt < ct:
            mt = ct
    res = d / mt
    fout.write(str(res))
    fout.write('\n')
    