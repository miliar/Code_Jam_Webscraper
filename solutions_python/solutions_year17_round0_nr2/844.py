import sys


def last_tidy(x):
    x = list(x)
    for i in range(len(x) - 1, 0, -1):
        if int(x[i - 1]) > int(x[i]):
            x[i - 1], x[i] = str(int(x[i - 1]) - 1), '9'
    res = []
    skip_zero = True
    append_nine = False
    for c in x:
        if append_nine:
            res.append('9')
        else:
            if c == '0':
                if not skip_zero:
                    res.append(c)
            else:
                skip_zero = False
                res.append(c)
                if c == '9':
                    append_nine = True
    return ''.join(res)


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        next(f)  # skip header

        for i, line in enumerate(f):
            x = line.strip()
            print('Case #{}: {}'.format(i + 1, last_tidy(x)))
