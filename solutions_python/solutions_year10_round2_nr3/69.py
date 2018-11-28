import sys

fin = sys.stdin
T = int(fin.readline())

ans = [0, 0, 1,
2,
3,
 5,
 8,
 14,
 24,
 43,
 77,
 140,
 256,
 472,
 874,
 1628,
 3045,
 5719,
 10780,
 20388,
 38674,
 73562,
 140268,
 268066,
 513350,
 984911]

for t in xrange(1, T + 1):
    print 'Case #' + str(t) + ':', (ans[int(fin.readline())] % 100003)
