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


def solve(n, m, a):
    for i in range(n):
        a[i] = list(a[i])

    last_colored = -1

    for i in range(n):
        colour = None

        for j in range(m):
            if a[i][j] != '?':
                if colour is None:
                    for k in range(j - 1, -1, -1):
                        a[i][k] = a[i][j]

                colour = a[i][j]

            if colour is not None:
                a[i][j] = colour

        if colour:
            for k in range(last_colored + 1, i):
                a[k] = a[i]

            last_colored = i

    for i in range(last_colored + 1, n):
        a[i] = a[last_colored]

    for i in range(n):
        a[i] = ''.join(a[i])

    return '\n'.join(a)


def main():
    testcases = next_int()

    for tc in range(1, testcases + 1):
        n = next_int()
        m = next_int()
        a = []
        for i in range(n):
            a.append(next_token())

        result = solve(n, m, a)

        cout.write('Case #%i:\n%s\n' % (tc, str(result)))


if __name__ == '__main__':
    main()