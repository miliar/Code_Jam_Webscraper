#!/usr/bin/python3 -t


def read_ints():
    return map(int, input().split())


def solve():
    n, x = read_ints()
    sizes = list(reversed(sorted(read_ints())))
    result = 0
    cur = []
    for s in sizes:
        ok = False
        for i, c in enumerate(cur):
            if s <= c:
                del cur[i]
                ok = True
                break
        if not ok:
            if x - s > 0:
                cur.append(x - s)
            result += 1
    print(result)


if __name__ == '__main__':
    for test_case in range(int(input())):
        print('Case #{}: '.format(test_case + 1), end='')
        solve()