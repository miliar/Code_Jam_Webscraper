t = int(raw_input())

for a0 in range(1, t+1):
    n, k = map(int,raw_input().strip().split())

    log = len(bin(k)) - 3

    den = 2 ** log

    sel = (den) - 1

    q = (n - sel) / den

    r = (n - sel) % den

    if (k - sel) <= r:
        q += 1

    #print q

    mini = ((q + 1) / 2) - 1

    maxi = (q - mini - 1)

    print 'Case #{}: {} {}'.format(a0, maxi, mini)

