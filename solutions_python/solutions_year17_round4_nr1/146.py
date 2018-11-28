import sys


#cin = open('input.txt', 'r')
#cin = open('A-small-attempt0.in', 'r')
cin = open('A-large.in', 'r')
#cin = sys.stdin
cout = open('output.txt', 'w')
#cout = sys.stdout

current_str_iter = None


def next_token():
    global current_str_iter

    while True:
        if current_str_iter is not None:
            token = next(current_str_iter, None)
            if token is not None:
                return token

        current_str_iter = iter(cin.readline().split())


def next_int():
    return int(next_token())


def solve2(a):
    return a[0] + a[1] / 2 + a[1] % 2


def solve3(a):
    result = a[0]
    result += min(a[1], a[2])

    remnant = a[1] + a[2] - 2 * min(a[1], a[2])

    result += remnant / 3
    if remnant % 3 > 0:
        result += 1

    return result


def solve4(a):
    result = a[0]
    result += a[2] / 2
    result += min(a[1], a[3])

    remnant = a[1] + a[3] - 2 * min(a[1], a[3])

    if a[2] % 2 == 1 and remnant >= 2:
        result += 1
        remnant -= 2
        a[2] -= 1

    result += remnant / 4
    if remnant % 4 > 0 or a[2] % 2 == 1:
        result += 1

    return result


def solve():
    n = next_int()
    p = next_int()

    a = []
    for i in range(p):
        a.append(0)

    for i in range(n):
        a[next_int() % p] += 1

    if p == 2:
        return solve2(a)
    elif p == 3:
        return solve3(a)
    elif p == 4:
        return solve4(a)
    else:
        return 1


def main():
    testcases = next_int()

    for tc in range(1, testcases + 1):
        result = solve()

        cout.write('Case #%i: %s\n' % (tc, str(result)))


if __name__ == '__main__':
    main()