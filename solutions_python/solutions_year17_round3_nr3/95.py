import math

fin = open('C-small-1-attempt0.in', 'r')
fout = open('C-small-1-attempt0.out', 'w')

t = int(fin.readline())
for i in xrange(1, t + 1):
    n, k = [int(ssss) for ssss in fin.readline().strip().split(" ")]
    u = float(fin.readline())
    p = [float(ssss) for ssss in fin.readline().strip().split(" ")]

    p = sorted(p, reverse = True)

    s = sum(p) + u
    for j in range(len(p)):
        if p[j] > s / n:
            s -= p[j]
            n -= 1
        else:
            p[j] = s / n

    ans = 1.0
    for j in p:
        ans *= j

    print>>fout, "Case #{}: {}".format(i, ans)

fin.close()
fout.close()
