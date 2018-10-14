from math import sqrt, floor, ceil


def main():
    with open('input.in', 'r') as f:
        tests = int(f.readline().strip())

        for x in xrange(tests):
            li, lf = [int(i) for i in f.readline().strip().split(" ")]

            print("Case #%d: %s" % (x+1, solve(li, lf)))


def solve(li, lf):
    sq_li = int(ceil(sqrt(li)))
    sq_lf = int(floor(sqrt(lf)))

    count = 0
    for x in xrange(sq_li, sq_lf+1):
        if is_pal(x) and is_pal(x*x):
            count += 1

    return count


def is_pal(a):
    return str(a)[::-1] == str(a)


if __name__ == '__main__':
    main()
