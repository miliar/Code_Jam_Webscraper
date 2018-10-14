import sys


def is_tidy(n, limit):
    last = '0'
    limit = str(limit)

    for digit in str(n):
        if digit < last or digit > limit:
            return
        last = digit

    return True


def compute_tidy(n, limit):
    if len(n) <= 1 or int(n) == 0:
        return min(n, str(limit))

    if is_tidy(n, limit):
        return n

    digit = min(n[-1], str(limit))
    digits = len(n)
    possibilities = set()

    if is_tidy(n[:-1] + digit, limit):
        possibilities.add(n[:-1] + digit)
    else:
        possibilities.add(make_tidy(n[:-1], limit=int(digit)) + digit)

    n = str(int(n) - int(n[-1]) - 1)
    if len(n) < digits:
        n = '0' + n

    possibilities.add(make_tidy(n[:-1]) + n[-1])

    return max(possibilities)


tidy_answers = {}


def make_tidy(n, limit=9):
    if (n, limit) not in tidy_answers:
        tidy_answers[(n, limit)] = compute_tidy(n, limit)

    return tidy_answers[(n, limit)]


def read_input():
    num_rows = int(sys.stdin.readline())

    for i in range(1, num_rows + 1):
        line = sys.stdin.readline().strip()
        result = make_tidy(line).lstrip('0')

        print('Case #{}: {}'.format(i, result))


read_input()
