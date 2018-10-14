def get_needed_friends(shy_people):
    total_standing = 0
    total_needed = 0

    for shy_level, people in enumerate(shy_people[:-1]):
        total_standing += people

        if total_standing < shy_level + 1:
            needed = shy_level + 1 - total_standing
            total_needed += needed
            total_standing += needed

    return total_needed


def compute_result(input_file, output_file):
    with open(input_file) as file, open(output_file, 'w') as result_file:
        nr_of_tests = int(file.readline())

        for case in range(1, nr_of_tests + 1):
            test_line = file.readline()
            max_shyness, people = test_line.split(sep=' ')

            needed_friends = get_needed_friends([int(i) for i in people if i.isdigit()])

            result_file.write('Case #%d: %d\r\n' % (case, needed_friends))


if __name__ == '__main__':
    compute_result('input.txt', 'result.txt')
