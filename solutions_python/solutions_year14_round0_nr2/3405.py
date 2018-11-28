#! /usr/bin/env python


def count_total_time(farms_count, c, f, x):
    total_time = 0.0

    for i in xrange(farms_count):
        total_time += c / (2.0 + i * f)

    total_time += x / (2.0 + farms_count * f)
    return total_time


def count_fastest_time(c, f, x):
    farms_count = 0
    current_fastest_time = None
    while True:
        t = count_total_time(farms_count, c, f, x)
        if current_fastest_time is None:
            current_fastest_time = t
            continue
        if t > current_fastest_time:
            return current_fastest_time
        else:
            current_fastest_time = t
            farms_count += 1


def print_results(f, results):
    with open(f, 'w') as output:
        for k, v in results.iteritems():
            output.write('Case #{0}: {1}\n'.format(k + 1, v))


def main():
    results = {}

    with open('data/problem_b.input', 'r') as input_file:
        test_cases = int(input_file.readline())
        for i in xrange(test_cases):
            line = input_file.readline().rstrip('\n').split(' ')
            c, f, x = float(line[0]), float(line[1]), float(line[2])
            results.setdefault(
                i,
                count_fastest_time(c, f, x),
            )

    print_results("data/problem_b.output", results)


if __name__ == '__main__':
    main()
