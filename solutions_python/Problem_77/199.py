import sys
def f(i, x):
    print "Case #%s: %s.000000" % (i, sum(1 for z in [int(c) - (i + 1) for i, c
        in enumerate(x.split())] if z != 0))

b = open(sys.argv[1]).readlines()

for i in range(int(b[0])):
    f(i + 1, b[i * 2 + 2])
