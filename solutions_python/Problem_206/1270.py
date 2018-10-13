import sys


def solve(d, n, k, s):
    # TODO Solve the problem

    left = 1.0
    right = 1.1e13
    mid = (left + right) / 2

    while abs((right - left) / mid) > 1e-6 and abs(right - left) > 1e-6:
        mid = (right + left) / 2
        mine = d / mid
        ok = True

        for i in range(n):
            elapsed = float(d - k[i]) / s[i]

            if mine < elapsed:
                ok = False
                break

        if ok:
            left = mid
        else:
            right = mid

    rv = (left + right) / 2

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
    line = lines.pop(0)
    d, n = line.split()
    d, n = int(d), int(n)

    k = list()
    s = list()

    for _ in range(n):
        x, y = lines.pop(0).split()

        k.append(int(x))
        s.append(int(y))

    answer = solve(d, n, k, s)

    print('Case #{0}: {1}'.format(i, answer))
""" Interpret the arguments """
