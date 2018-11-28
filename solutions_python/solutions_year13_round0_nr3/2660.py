from math import sqrt


def is_palindrom(n):
    n_str = str(n)
    for i in xrange(len(n_str) / 2):
        if n_str[i] != n_str[-(i + 1)]:
            return False
    return True


def count_fair_and_square(a, b):
    '''
    @return: (int).
    '''
    count = 0
    for i in xrange(a, b + 1):
        root = sqrt(i)
        if root != int(root):
            continue
        root = int(root)
        if not is_palindrom(i) or not is_palindrom(root):
            continue
        count += 1

    return count


if __name__ == '__main__':
    input_file = open('C-small-attempt0.in', 'r')
    output_file = open('C-small-attempt0.out', 'w')

    test_cases_count = int(input_file.readline())

    for line_number in range(test_cases_count):
        a, b = input_file.readline().strip().split(' ')
        a = int(a)
        b = int(b)

        output_file.write('Case #%d: %s\n' % \
                          (line_number + 1, count_fair_and_square(a, b)))

    input_file.close()
    output_file.close()
