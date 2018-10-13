import sys
import math


class Solution:
    def process(self, n, k, r, h):
        data = []
        for i in range(n):
            data.append((-2 * r[i] * h[i], r[i], h[i]))
        data.sort()
        max_value = 0
        for i in range(n):
            total = data[i][1] ** 2 - data[i][0]
            total_count = 0
            for j in range(k + 1):
                if j != i:
                    total_count += 1
                    if total_count > k - 1: break

                    total -= data[j][0]

            if total > max_value:
                max_value = total

        return max_value * math.pi


# INPUT_FILE_NAME = 'input.in'
INPUT_FILE_NAME = 'A-large.in'
OUTOUT_FILE_NAME = 'a-small.out'

fi = open(INPUT_FILE_NAME, 'r')
fo = open(OUTOUT_FILE_NAME, 'w')

number_test = int(fi.readline())
for t in xrange(1, number_test + 1):
    n, k = [int(s) for s in fi.readline().split(" ")]
    r, h = [], []
    for i in range(n):
        rr, hh = [int(s) for s in fi.readline().split(" ")]
        r.append(rr)
        h.append(hh)

    result = Solution().process(n, k, r, h)

    fo.write("Case #%s: %s\n" % (t, result))

fi.close()
fo.close()
