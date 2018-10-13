from math import log

T = int(raw_input())
for t in xrange(1, T + 1):
    N, K = map(int, raw_input().split(' '))
    K = K - 1

    layer = int(log(K + 1, 2))
    Ktook = (2 ** layer) - 1
    Kleft = K - Ktook
    stalls_left = N - Ktook
    values = stalls_left / (2 ** layer)
    num_higher_values = stalls_left - (values * (2 ** layer))

    num_higher_values = max(0, num_higher_values - Kleft)

    n = values
    if num_higher_values > 0:
        n += 1

    print 'Case #{}: {} {}'.format(t, n / 2, (n - 1) / 2)
