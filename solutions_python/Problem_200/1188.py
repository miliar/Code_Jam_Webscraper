import sys


def is_tidy(digits):
    x = 0

    for y in digits:
        if y < x:
            return False

        x = y

    return True


def solve(n):
    # TODO Solve the problem
    digits = list()
    original = n

    while n > 0:
        d = n % 10

        digits.insert(0, d)

        n /= 10

    if is_tidy(digits):
        return original

    pos = 0
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            pos = i + 1

    for i in reversed(range(pos)):
        digits[i] -= 1

        if i > 0:
            if digits[i] >= digits[i - 1]:
                break
            else:
                digits[i] = 9

    for i in range(pos, len(digits)):
        digits[i] = 9

    clean = list()
    start = False

    for x in digits:
        if start:
            clean.append(x)
        elif x > 0:
            clean.append(x)
            start = True

    sz = len(clean)

    rv = 0

    for i in range(len(clean)):
        rv += int(clean[i] * pow(10, sz - i - 1))

    return rv


""" Convert the input file into a list of strings """
in_file = sys.argv[1]

with open(in_file, "r") as f:
    data = f.read()

lines = data.splitlines()
""" Convert the input file into a list of strings """

""" Interpret the arguments """
cases = int(lines.pop(0))

for i in range(1, cases + 1):
    line = int(lines.pop(0))

    answer = solve(line)

    print 'Case #%d: %s' % (i, answer)
""" Interpret the arguments """
