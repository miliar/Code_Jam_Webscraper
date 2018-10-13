t = int(raw_input())

for a0 in range(1, t+1):
    a = map(int,list(raw_input().strip()))

    #print a

    l = len(a)

    x = l

    if len(a) == 1:
        print 'Case #{}: {}'.format(a0, a[0])
        continue

    for i in range(l-1, 0, -1):
        if a[i-1] > a[i]:
            a[i-1] -= 1
            for j in range(i, x):
                a[j] = 9
            x = i

    ans = int(''.join(str(i) for i in a))
    print 'Case #{}: {}'.format(a0, ans)

