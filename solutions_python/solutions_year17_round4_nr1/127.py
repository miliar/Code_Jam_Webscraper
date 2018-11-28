# coding: utf8

import sys
import math


def main():
    T = int(sys.stdin.readline())
    for _T in range(T):
        N, P = map(int, sys.stdin.readline().split())
        groups = [
            int(x)
            for x in sys.stdin.readline().strip().split()
        ]
        groups = [x % P for x in groups]
        counts = [groups.count(x) for x in range(P)]
        if P == 2:
            ans = counts[0] + math.ceil(counts[1] / 2.0)
        elif P == 3:
            ans = counts[0] + min(counts[1], counts[2])
            ans += math.ceil((max(counts[1], counts[2]) - min(counts[1], counts[2])) / 3.0)
        elif P == 4:
            ans = counts[0] + min(counts[1], counts[3]) + counts[2] // 2
            remainder = max(counts[1], counts[3]) - min(counts[1], counts[3])
            if counts[2] % 2:
                ans += 1
                ans += max(0, math.ceil((remainder - 2) / 4.0))
            else:
                ans += math.ceil(remainder / 4.0)
        print('Case #%s: %s' % (_T + 1, ans))


if __name__ == '__main__':
    main()
