from math import log, floor, ceil

for j in range(int(input())):
    N, K = map(int, input().split())
    if K == 1:
        l = 1
    else:
        l = 2**floor(log(K, 2))
    if N - K == 0:
        x = 0
    else:
        x = ceil((N - K + 1) / l) - 1
    print('Case #' + str(j + 1) + ': ' +
          str(ceil(x / 2)) + ' ' + str(floor((x / 2))))
