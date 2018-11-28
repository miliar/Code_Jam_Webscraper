# coding: utf8

import sys


def main():
    T = int(sys.stdin.readline())
    for _T in range(T):
        N, P = list(map(int, sys.stdin.readline().split()))
        needed = list(map(int, sys.stdin.readline().split()))
        packs = [
            list(map(int, sys.stdin.readline().split()))
            for i in range(N)
        ]
        def get_range(i, j):
            ret = [
                packs[i][j] * 100 // (needed[i] * 110),
                packs[i][j] * 100 // (needed[i] * 90),
            ]
            ret = [
                k
                for k in range(ret[0], ret[1] + 1)
                if needed[i] * k * 90 <= packs[i][j] * 100 <= needed[i] * k * 110
            ]
            return [
                min(ret or [0]),
                max(ret or [0]),
            ]
        packs_n = [
            [
                get_range(i, j)
                for j in range(P)
            ]
            for i in range(N)
        ]
        packs_n = [
            sorted(x)
            for x in packs_n
        ]
        def join(range1, range2):
            if range1[0] <= range2[0] <= range1[1] or range2[0] <= range1[0] <= range2[1]:
                return True
            return False
        result = 0
        used = [-1 for i in range(N)]
        for k in range(P):
            tmpr = packs_n[0][k]
            candidate = [[] for i in range(N)]
            candidate[0] = [k]
            for i in range(1, N):
                for j in range(used[i] + 1, P):
                    if join(tmpr, packs_n[i][j]):
                        candidate[i].append(j)
            if all(candidate):
                tmpr[0] = max(
                    min(
                        packs_n[i][j][0]
                        for j in candidate[i]
                    )
                    for i in range(N)
                )
                tmpr[1] = min(
                    max(
                        packs_n[i][j][1]
                        for j in candidate[i]
                    )
                    for i in range(N)
                )
                if 0 < tmpr[0] <= tmpr[1]:
                    for i in range(N):
                        used[i] = candidate[i][0]
                    result += 1
                else:
                    pass
        print('Case #%s: %s' % (_T + 1, result))


if __name__ == '__main__':
    main()
