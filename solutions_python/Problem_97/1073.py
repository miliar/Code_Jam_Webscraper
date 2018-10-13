__author__ = 'Janek Krukowski'

def count_digits(num):
    ret = 0
    while num:
        ret += 1
        num = num / 10
    return ret

def get_number(num, comb_count):
    p = pow(10, comb_count-1)
    for i in xrange(comb_count-1):

        d = num / p
        r = num % p
        num = (r*10) + d
        yield num


def solve_case(start, stop):
    ret = 0
    for num in xrange(start, stop):
        d = count_digits(num)
        if d <= 1:
            continue

        for cnum in get_number(num, d):
            if num < cnum and cnum <= stop:
                ret += 1
    return ret


def main():
    with open('C-small-attempt0.in', 'r') as input, open('output.out', 'w') as output:
        cases = int(input.readline())
        for i in xrange(cases):
            line = [int(k) for k in input.readline().split(' ')]
            output.write('Case #{0}: {1}\n'.format(i+1, solve_case(line[0], line[1])))


if __name__ == '__main__':
    main()
