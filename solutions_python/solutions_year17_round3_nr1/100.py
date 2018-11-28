import sys
from math import pi

# sys.stdin = open('a1.in')
# sys.stdin = open('A-small-attempt1.in')
sys.stdin = open('A-large.in')
sys.stdout = open('out.txt', 'w')


def read_int():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def solve_it():
    n, k = read_int_list()
    p = []
    for i in range(n):
        r, h = read_int_list()
        p.append((r * h, r, h))
    p.sort(reverse=True)
    if k == 1:
        return max([pi * r ** 2 + 2 * pi * r * h for (rh, r, h) in p])

    res = 0
    for i in range(n):
        if i + k - 2 <= n - 1:
            s = 0
            rm = 0
            for j in range(i, i + k - 1):
                s += 2 * pi * p[j][1] * p[j][2]
                rm = max(rm, p[j][1])
            found = False
            max_bottom = 0
            for j in range(n):
                if i <= j < i + k - 1:
                    continue
                if p[j][1] >= rm:
                    found = True
                    diff = 2 * pi * p[j][1] * p[j][2] + pi * (p[j][1] ** 2)
                    max_bottom = max(max_bottom, diff)
            if found:
                s += max_bottom
                if res < s:
                    res = s
    return res


def solve_it2():
    n, k = read_int_list()
    p = []
    for i in range(n):
        r, h = read_int_list()
        p.append((r, h))
    res = 0
    for i in range(n):
        ri, hi = p[i]
        a = []
        for j in range(n):
            if j != i:
                r, h = p[j]
                if r <= ri:
                    a.append((r * h, r, h))
        a.sort(reverse=True)
        if len(a) >= k - 1:
            t = pi * ri ** 2 + 2 * pi * ri * hi
            for j in range(k - 1):
                t += 2 * pi * a[j][0]
            if t > res:
                res = t
    return res


def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it2()
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)


if __name__ == '__main__':
    main()
