from sys import stdin, stdout

n = int(stdin.readline().strip())
case = 1
for i in xrange(n):
    values = map(int, stdin.readline().strip().split())
    n = values[0]
    s = values[1]
    p = values[2]
    scores = values[3:]
    count = 0
    for score in scores:
        mod = score%3
        parted = score/3
        if mod == 0:
            if parted >= p:
                count += 1
            elif parted > 0 and parted+1 >= p and s > 0:
                count += 1
                s -= 1
        elif mod == 1:
            if parted >= p or parted+1 >= p:
                count += 1
            elif s > 0 and parted+1 >= p:
                count += 1
                s -= 1
        else:
            if parted+1 >= p or parted >= p:
                count += 1
            elif parted+2 >= p and s > 0:
                count += 1
                s -= 1
    print 'Case #%d: %d' %(case, count)
    case += 1
