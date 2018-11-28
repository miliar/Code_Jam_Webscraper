from math import log, ceil

fin = open("B-small-attempt3.in", "r")
fout = open("B-small-attempt3.out", "w")

T = int(fin.readline())

for t in xrange(T):
    L, P, C = [int(i) for i in fin.readline().split()]
    lower = log(L, C)
    upper = log(P, C)
    diff = upper - lower
    a = ceil(log(diff, 2) - 0.0001)
    if a < 0: a = 0
    print L, P, C, ":", a, log(diff, 2)
    fout.write("Case #%i: %i\n" % (t + 1, a))

fin.close()
fout.close()
