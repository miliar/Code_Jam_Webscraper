import math

fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

t = int(fin.readline())
for i in xrange(1, t + 1):
    ans = 1000000000000000
    d, n = [int(s) for s in fin.readline().strip().split(" ")]
    for j in range(n):
        k, s = [int(s) for s in fin.readline().strip().split(" ")]
        t = (d - k) * 1.0 / s
        speed = d * 1.0 / t
        if ans > speed:
            ans = speed
    print>>fout, "Case #{}: {}".format(i, ans)

fin.close()
fout.close()
