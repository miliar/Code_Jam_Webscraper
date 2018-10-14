for t in range(int(raw_input())):
    n, r, o, y, g, b, v = map(int,raw_input().strip().split())

    m = max(r, y, b)

    if m > n/2:
        print 'Case #{}: IMPOSSIBLE'.format(t + 1)
        continue

    arr = [[r, 'r'], [y, 'y'], [b, 'b']]

    arr = sorted(arr, key = lambda x:x[0], reverse=True)

    #print arr

    rem_a = m - arr[2][0]
    ab = m - arr[2][0]
    abc = arr[1][0] - rem_a
    ac = arr[2][0] - abc

    ans = ''
    for i in range(ab):
        ans = ans + arr[0][1] + arr[1][1]

    for i in range(ac):
        ans = ans + arr[0][1] + arr[2][1]

    for i in range(abc):
        ans = ans + arr[0][1] + arr[1][1] + arr[2][1]

    print 'Case #{}: {}'.format(t+1, ans)