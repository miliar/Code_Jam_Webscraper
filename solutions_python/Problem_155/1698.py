from __future__ import print_function

from sys import exit, stdin, stdout


def solve():
    """Main."""
    _, people = read_array()
    friends = 0
    up = 0
    for shyness, men in enumerate(people):
        men = int(men)
        if shyness == 0:
            up += men
        else:
            if shyness > up:
                friends += shyness - up
                up += shyness - up
            up += men
    write(friends)


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
