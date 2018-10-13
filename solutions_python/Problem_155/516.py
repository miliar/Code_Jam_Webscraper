for test in range(int(input())):
    sm, hist = input().split()
    sm = int(sm)

    ans = 0
    so_far = int(hist[0])
    for i in range(1, sm + 1):
        cur = int(hist[i])

        if so_far < i:
            ans += i - so_far
            so_far = i

        so_far += cur

    print('Case #%d: %d' % (test + 1, ans))

