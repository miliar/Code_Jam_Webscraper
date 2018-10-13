for t in range(int(input())):
    li = list(map(int, list(input().split()[1])))
    z = 0
    res = 0
    for i in range(len(li)):
        if i > z:
            res += i - z
            z = i
        z += li[i]
    print('Case #%d: %s' % (t + 1, res))
