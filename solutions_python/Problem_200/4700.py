import sys


def _is_tidy(number):
    prev = number % 10

    while number > 0:
        n = number % 10

        if n > prev:
            return False

        prev = n

        number = number // 10

    return True


def _last_tidy(n):
    for i in range(n, 0, -1):
        if _is_tidy(i):
            return i

    raise Exception('Could not find tidy number')


with open(sys.argv[1]) as f_in:
    with open(sys.argv[2], 'wt') as f_out:
        next(f_in)

        for i, line in enumerate(f_in):
            last = _last_tidy(int(line))

            f_out.write('Case #{}: {res}\n'.format(i + 1, res=last))
            print('Case #{}: {res}'.format(i + 1, res=last))

print('~FIN~')
