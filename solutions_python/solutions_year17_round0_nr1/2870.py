INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'


def process_input_line(line):
    pancakes, k = line.strip().split(" ")
    return (pancakes, int(k))

def flip_pancakes(pancakes):
    result = ''
    for i in pancakes:
        if i == '+':
            result += '-'
        elif i == '-':
            result += '+'
    return result


def solve_test(input_data):
    pancakes, k = input_data
    if pancakes.count('+') == len(pancakes):
        return 0

    p = pancakes

    print 'pancakes:', p

    counter = 0
    for i in xrange(len(pancakes) - k + 1):
        if p[i] == '+':
            continue

        counter += 1
        p = '{0}{1}{2}'.format(
            p[:i],
            flip_pancakes(p[i:i+k]),
            p[i+k:]
        )
        print 'pancakes:', p, counter

        if p.count('+') == len(p):
            return counter

    return 'IMPOSSIBLE'


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
