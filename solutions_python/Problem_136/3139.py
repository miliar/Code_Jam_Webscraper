from math import floor
import sys


def main():
    filename = sys.argv[1]
    cookie_clicker(filename)


def get_number_of_farms(c, f, x):
    n = int(floor((x / c) - (2 / f)))
    return n if n > 0 else 0


def time_to_x(n, c, f, x):
    t = (sum([(c / float(2 + a * f)) for a in range(0, n)]) +
         (x / float(2 + n * f)))
    return t


def read_cookie_vars(fileobj):
    c, f, x = [float(a) for a in fileobj.readline().split(' ')]
    return c, f, x


def print_result(min_time, case_number):
    print('Case #{case}: {time}'.format(case=case_number, time=min_time))


def cookie_clicker(filename):

    with open(filename, 'r') as fileobj:
        num_tests = int(fileobj.readline())
        for i in range(1, num_tests + 1):
            c, f, x = read_cookie_vars(fileobj)
            n = get_number_of_farms(c, f, x)
            t = time_to_x(n, c, f, x)
            print_result(t, i)


if __name__ == '__main__':
    main()
