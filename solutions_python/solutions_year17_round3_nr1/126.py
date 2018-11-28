import math

fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

t = int(fin.readline())
for i in xrange(1, t + 1):
    n, k = [int(ssss) for ssss in fin.readline().strip().split(" ")]
    rh = []
    for j in range(n):
        r, h  = [int(ssss) for ssss in fin.readline().strip().split(" ")]
        rh.append((r, math.pi * r * h * 2))
    rh = sorted(rh, key=lambda x:x[1], reverse=True)
    max = 0
    for j in range(n):
        tmp = []
        if k-1 < j:
            tmp = rh[0: k-1]
            tmp.append(rh[j])
        else:
            tmp = rh[0: k]
        s = math.pi * sorted(tmp, key=lambda x:x[0], reverse=True)[0][0] * sorted(tmp, key=lambda x:x[0], reverse=True)[0][0]
        for u in range(k):
            s += tmp[u][1]
        if max < s:
            max = s

    print>>fout, "Case #{}: {}".format(i, max)

fin.close()
fout.close()
