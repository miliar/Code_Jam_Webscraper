INPUT_FILE = 'B-large.in'
OUTPUT_FILE = 'B-large.out'


def process_input_line(line):
    return int(line.strip())


def is_tidy(n):
    str_n = str(n)
    if len(str_n) == 1:
        return True

    prev_i = str_n[0]
    for i in str_n:
        if int(i) < int(prev_i):
            return False
        prev_i = i

    return True


def decrement_digit_at_pos(value, pos):
    s = str(value)
    a = int(s[:pos+1]) - 1
    return '{0}{1}'.format(a, s[pos+1:])


def find_tidy(n):
    s = str(n)
    v = s

    if is_tidy(int(v)):
        return v

    v = '{0}{1}'.format(
        s[:-1],
        9
    )
    if (int(v) < n) and is_tidy(int(v)):
        return v

    for i in xrange(len(s) - 2, -1, -1):
        v = decrement_digit_at_pos(int(v), i)
        if (int(v) < n) and is_tidy(int(v)):
            return v

        v = '{0}{1}{2}'.format(
            v[:i],
            9,
            v[i+1:]
        )
        if (int(v) < n) and is_tidy(int(v)):
            return v


def solve_test(input_data):
    n = input_data
    if is_tidy(n):
        return n
    return int(find_tidy(n))


def read_data(input_file):
    total_tests = None
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            if total_tests is None:
                total_tests = int(line.strip())
            else:
                data += [process_input_line(line)]
    return total_tests, data


def find_solution(data, output_file):
    solution = []
    for i, item in enumerate(data):
        solution += ['Case #{0}: {1}\n'.format(
            i + 1,
            solve_test(item)
        )]
    with open(output_file, 'wb') as f:
        f.writelines(solution)


def main():
    total_tests, data = read_data(INPUT_FILE)

    print 'total_tests', total_tests
    for i in data:
        print i

    if total_tests != len(data):
        raise Exception('Number of tests {0}, expected {1}'.format(
            len(data),
            total_tests
        ))

    find_solution(data, OUTPUT_FILE)

if __name__ == '__main__':
    main()
