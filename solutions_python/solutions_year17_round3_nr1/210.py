
import math
import copy

t = int(raw_input())

for case in range(t):

    n, k = [int(s) for s in raw_input().split()]
    opt = []

    for l in range(n):
        i, j = [float(s) for s in raw_input().split()]
        tmp = []
        tmp.append(i)
        tmp.append(j)
        tmp.append(i * i * math.pi)
        tmp.append(2 * i * math.pi * j)
        opt.append(tmp)

    opt.sort(key=lambda x: x[2], reverse=True)

    ans = 0.0

    for i in range(n - k + 1):
        tmp = copy.deepcopy(opt[i + 1:])
        tmp.sort(key=lambda x: x[3], reverse=True)
        num = opt[i][2] + opt[i][3]
        for j in range(k - 1):
            num += tmp[j][3]

        if num > ans:
            ans = num

    print 'Case #%d: %.9f' % (case + 1, ans)








