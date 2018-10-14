from math import log, ceil

def is_power_of_two(x):
    a = log(x, 2)

    return float(int(a)) == a

def decompose(a, b):
    i = 2

    while i <= min(a, b):
        if a % i == b % i == 0:
            a, b = a / i, b / i
        i += 1

    return a, b

def solve(a, b):
    a, b = decompose(a, b)

    if not is_power_of_two(b):
        return 'impossible'

    inv = float(b) / float(a)
    l = log(inv, 2)

    return int(ceil(l))

if __name__ == '__main__':
    T = input()

    for case in xrange(T):
        p, q = [int(a) for a in raw_input().split('/')]

        print 'Case #{}: {}'.format(case+1, solve(p, q))
