N = input()
for i in range(1, N + 1):
    x = raw_input().split(' ')
    a, b, k = int(x[0]), int(x[1]), int(x[2])
    ans = 0
    for ax in range(0, a):
        for bx in range(0, b):
            if ax & bx < k: ans += 1
    print 'Case #{0}: {1}'.format(i, ans)
