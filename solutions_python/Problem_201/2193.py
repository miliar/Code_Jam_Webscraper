import math
T = int(input())
for test_case in range(1, T+1):
    N, K = [int(i) for i in input().split()]
    kLog = int(math.log2(K))
    newK = 2**kLog
    kDiff = K - newK
    newN = N - kDiff
    last = newN // newK
    if last % 2 == 0:
        factor = last // 2
        one, two = factor, factor-1
    else:
        factor = (last-1) // 2
        one, two = factor, factor
    print("Case #{}: {} {}".format(test_case, one, two))

