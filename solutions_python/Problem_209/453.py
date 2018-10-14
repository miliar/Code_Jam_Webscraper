import sys
import math
input = open(sys.argv[1])


def solve(n, k):
    ans = 0
    s = [[float(x) for x in input.readline().split()] for _ in range(n)]
    area = [2 * math.pi * x[0] * x[1] for x in s]
    for i in range(n):
        tmp = s[i][0] * s[i][0] * math.pi + area[i]
        tmp += sum(sorted(area[:i] + area[i + 1:], reverse=True)[:k - 1])
        ans = max(ans, tmp)
    return ans

for case in range(int(input.readline())):
    s, k = input.readline().split()
    print ("Case #%d: %.9f" % (case + 1, solve(int(s), int(k))))
