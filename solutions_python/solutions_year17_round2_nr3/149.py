#!/usr/bin/env python3

import functools


def solve():
    n, q = map(int, input().split())
    e = [0]*n
    s = [0]*n
    u = [0]*q
    v = [0]*q
    for i in range(n):
        e[i], s[i] = map(int, input().split())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(q):
        u[i], v[i] = map(int, input().split())

    @functools.lru_cache(maxsize=100500)
    def solve_simple(start, end, cur_speed, cur_maydist):
        #print(start, end, cur_speed, cur_maydist)
        if cur_maydist < 0:
            return None
        if start == end:
            return 0
        diff = 1
        if end < start:
            diff = -1
        var1 = solve_simple(
                start+diff, end, cur_speed, cur_maydist-d[start][start+diff])
        if var1 is not None:
            var1 += d[start][start+diff]/cur_speed
        var2 = var1
        if cur_speed != s[start] or cur_maydist != e[start]:
            cur_speed = s[start]
            cur_maydist = e[start]
            var2 = solve_simple(
                start+diff, end, cur_speed, cur_maydist-d[start][start+diff])
            if var2 is not None:
                var2 += d[start][start+diff]/cur_speed
        if var1 is None:
            return var2
        if var2 is None:
            return var1
        return min(var1, var2)

    return solve_simple(u[i]-1, v[i]-1, s[u[i]-1], e[u[i]-1])

    res = [0]*q
    return " ".join(map(str, res))


def main():
    k = int(input())
    for i in range(k):
        print("Case #{}: {}".format(i + 1, solve()))

if __name__ == '__main__':
    main()
