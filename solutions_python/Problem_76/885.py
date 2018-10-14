__author__ = 'brunocatao'

import itertools

def solve_candy_split(values):
    val_max = -1
    indexes = list(range(len(values)))
    for i in range(1, len(values)):
        for comb in itertools.combinations(indexes, i):
            xor_sum1 = 0
            xor_sum2 = 0
            sum1 = 0
            sum2 = 0

            for j in indexes:
                if j in comb:
                    xor_sum1 ^= values[j]
                    sum1 += values[j]
                else:
                    xor_sum2 ^= values[j]
                    sum2 += values[j]

            if xor_sum1 == xor_sum2:
                val_max = max(val_max, max(sum1, sum2))
    return val_max

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        raw_input()
        result = solve_candy_split(map(int, raw_input().split()))
        if result >= 0:
            print "Case #%d: %d" % (i + 1, result,)
        else:
            print "Case #%d: NO" % (i + 1,)