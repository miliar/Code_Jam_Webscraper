import sys

tc_len = int(sys.stdin.readline())

for tc in range(tc_len):
    d, n = tuple(int(x) for x in sys.stdin.readline().split())
    h_max = 0
    for _ in range(n):
        k, s = tuple(int(x) for x in sys.stdin.readline().split())
        h = (d - k) / s
        h_max = max(h, h_max)
    print('Case #' + str(tc + 1) + ': ' + str(d / h_max))
