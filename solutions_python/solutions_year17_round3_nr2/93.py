import sys

# sys.stdin = open('b1.in')
# sys.stdin = open('B-small-attempt0.in')
sys.stdin = open('B-large.in')
sys.stdout = open('out.txt', 'w')


def read_int():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def solve_it():
    ac, aj = read_int_list()
    nm = 24 * 60
    a = [0] * nm
    remaining = [None, 720, 720]
    for i in range(ac):
        start, stop = read_int_list()
        for j in range(start, stop):
            a[j] = 1
        remaining[1] -= stop - start
    for i in range(aj):
        start, stop = read_int_list()
        for j in range(start, stop):
            a[j] = 2
        remaining[2] -= stop - start
    i0 = -1
    for i in range(nm):
        if a[i - 1] != 0 and a[i] == 0:
            i0 = i
            break
    if i0 == -1:
        res = 0
        for i in range(nm):
            if a[i - 1] != a[i]:
                res += 1
        return res

    s = [[], [], []]
    i = i0
    steps = 0
    while True:
        if a[i] == 0:
            left = a[i - 1]
            l = 0
            while a[i] == 0:
                l += 1
                i += 1
                i %= nm
                steps += 1
            right = a[i]
            if left != right:
                s[0].append(l)
            else:
                s[left].append(l)
        i += 1
        i %= nm
        steps += 1
        if steps == nm:
            break

    for i in range(nm):
        if a[i - 1] != 0 and a[i] != 0 and a[i - 1] != a[i]:
            s[0].append(0)

    s[1].sort()
    s[2].sort()
    res = 10 ** 12
    for k1 in range(len(s[1])+1):
        for k2 in range(len(s[2])+1):
            if sum(s[1][:k1]) <= remaining[1] and sum(s[2][:k2]) <= remaining[2]:
                rr = len(s[0]) + 2 * (len(s[1])-k1) + 2* (len(s[2])-k2)
                if rr < res:
                    res = rr
    return res


def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it()
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)


if __name__ == '__main__':
    main()
