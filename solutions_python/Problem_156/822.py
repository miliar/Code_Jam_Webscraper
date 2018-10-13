import sys

t = int(raw_input())

for i in range(0, t):
    d = int(raw_input())
    raw = sorted(map(int, raw_input().split()))
    l = list(raw)
    count = 0
    last = l[-1]
    res = last + count
    
    while last > 2:
        l = l[:-1]
        l.append(last/2)
        l.append(last - last/2)
        l = sorted(l)
        count += 1
        last = l[-1]
        if last + count < res:
            res = last + count

    l = list(raw)
    count = 0
    last = l[-1]
    while last > 3:
        l = l[:-1]
        l.append(3)
        l.append(last - 3)
        l = sorted(l)
        count += 1
        last = l[-1]
        if last + count < res:
            res = last + count

    # print res

    print "Case #" + str(i + 1) + ": " + str(res)