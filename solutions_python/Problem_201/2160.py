import math

num = int(raw_input())
for i in range(1, num+1):
    tmp = raw_input().split()
    stalls = int(tmp[0])
    n = int(tmp[1])

    l = [stalls]

    for j in range(n):
        if j == n - 1:
            l.sort()
            ind = l.pop()
            big = ind / 2
            small = ind - 1 - ind / 2

            print "Case #%d: %d %d" %(i, big, small)

        else:
            l.sort()
            ind = l.pop()
            l.append(ind / 2)
            l.append(ind - 1 - ind / 2)
