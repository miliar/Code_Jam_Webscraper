"""

"""

import sys

def is_tidy(n):

    s = str(n)
    return list(s) == sorted(s)


def make_tidy(n):

    if not is_tidy(n):
        s = str(n)
        while not s[-1] == '9':
            n -= 1
            s = str(n)

        if s[:-1]:
            s = make_tidy(int(s[:-1])) + '9'
        else:
            s = '9'

    else:

        s = str(n)

    return s


with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    test_cases = [int(s[:-1]) for s in f.readlines()]

tidy_numbers = []

for number in test_cases:

    tidy_numbers.append(make_tidy(number))

t = 1
with open(sys.argv[2], 'w') as f:
    for number in tidy_numbers:
        f.write("Case #%d: %s\n" % (t, number))
        t += 1
