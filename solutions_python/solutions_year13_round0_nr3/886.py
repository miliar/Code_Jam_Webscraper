def is_pal(number):
    direct = 0L
    tmp = number
    while tmp:
        direct = direct * 10 + tmp % 10
        tmp /= 10L
    return direct == number


def solve(file_name, out_file_name):
    out_file = open(out_file_name, 'w')
    in_file = open(file_name, 'r')

    cases = int(in_file.readline())

    master = filter(is_pal, map(
        lambda x: x ** 2,
        filter(is_pal, xrange(1, 10 ** 7))))

    for case in xrange(cases):
        out_file.write('Case #%d: ' % (case + 1))
        A, B = map(int, in_file.readline().split())
        out_file.write('%d\n' % (len(
            filter(lambda x: A <= x and x <= B, master)))
        )

    out_file.close()
    in_file.close()


if __name__ == '__main__':
    import sys
    file_name = sys.argv[1]
    out_file_name = sys.argv[2]
    solve(file_name, out_file_name)
