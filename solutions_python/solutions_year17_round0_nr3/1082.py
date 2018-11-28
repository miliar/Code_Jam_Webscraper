import math


def solve(N, K):
    index = 0

    while K >= pow(2, index):
        index += 1

    divider = pow(2, index)
    remainder = K - pow(2, index-1)
    s1 = math.floor((N - (divider - 1)) / divider)
    s1Remainder = (N - (divider - 1)) % divider
    s2 = s1 + math.floor(s1Remainder / pow(2, index-1))
    s2Remainder = s1Remainder % pow(2, index-1)
    if remainder < s2Remainder:
        s1 += 1
    return '' + str(max(s1, s2)) + ' ' + str(min(s1, s2))


T = int(input())
for i in range(T):
    N, K = [float(s) for s in input().split(" ")]
    print('Case #{}: {}'.format(i+1, solve(N, K)))
