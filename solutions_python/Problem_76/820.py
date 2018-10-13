for i in range(input()):
    n = input()
    l = [int(a) for a in raw_input().split()]
    sum = 0
    for j in range(n):
        sum ^= l[j]
    if sum == 0:
        l.sort()
        max = 0
        for j in range(n-1):
            max += l[j+1]
        res = 'Case #{0}: {1}'.format(i+1,max)
    else:
        res = 'Case #{0}: NO'.format(i+1)

    print res
