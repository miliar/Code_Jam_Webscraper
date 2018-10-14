from __future__ import print_function

from sys import exit, stdin, stdout


def solve():
    """Main."""
    x, n_rows, n_columns = read_int_array()

    n_rows, n_columns = min(n_rows, n_columns), max(n_rows, n_columns)

    if n_rows * n_columns % x:
        write('RICHARD')
    elif x == 1:
        write('GABRIEL')
    elif x == 2:
        write('GABRIEL')
    elif x == 3:
        if n_columns < 3 or n_rows == 1:
            write('RICHARD')
        else:
            write('GABRIEL')
    elif x == 4:
        if n_columns < 4 or n_rows in (1, 2):
            write('RICHARD')
        else:
            write('GABRIEL')
    else:
        raise ValueError


def main():
    for test in xrange(read_int()):
        write('Case #{}: '.format(test + 1), end='')
        solve()


def bye(message=None):
    if message is not None:
        write(message)
    exit()


def read(func=None):
    a = stdin.readline().rstrip('\n')
    return a if func is None else func(a)


def read_array(func=None, sep=None, maxsplit=-1):
    array = read().split(sep, maxsplit)
    return array if func is None else [func(a) for a in array]


def read_int():
    return read(int)


def read_int_array(sep=None, maxsplit=-1):
    return read_array(int, sep, maxsplit)


def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    stdout.write(sep.join(str(a) for a in args) + end)


def write_array(array, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    stdout.write(sep.join(str(a) for a in array) + end)


main()
