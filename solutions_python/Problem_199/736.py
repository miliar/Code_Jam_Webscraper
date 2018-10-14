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


def solve(a, k):
    for i in range(len(a)):
        a[i] = a[i] == '+'

    flips = 0

    for i in range(len(a) - k + 1):
        if not a[i]:
            flips += 1

            for j in range(i, i + k):
                a[j] = not a[j]

    for pancake in a:
        if not pancake:
            return 'IMPOSSIBLE'

    return flips



def main():
    testcases = next_int()

    for tc in range(1, testcases + 1):
        a = list(next_token())
        k = next_int()

        result = solve(a, k)

        cout.write('Case #%i: %s\n' % (tc, str(result)))


if __name__ == '__main__':
    main()