def get_input():
    f = open('example.in')
    contents = f.readlines()
    f.close()

    return contents


def get_data(name_file):
    f = open(name_file)

    # The first line gives the number of test cases
    test_cases = int(f.readline())
    data = []

    for i in range(test_cases):
        line = f.readline()
        (max_shyness, shyness_data) = line.split()
        max_shyness = int(max_shyness)
        data.append((max_shyness, shyness_data))

    return test_cases, data


def solve_problem(max_shyness, shyness_data):
    people_to_add = 0
    people_in_theater = 0

    for i in range(max_shyness + 1):
        num_shy_people_i = int(shyness_data[i])
        total_people = people_in_theater + people_to_add

        if total_people < i:
            people_to_add += (i - total_people)

        people_in_theater += num_shy_people_i

    return people_to_add


def solve(in_filename, out_filename):
    test_cases, data = get_data(in_filename)

    solutions = []

    for case in data:
        solutions.append(solve_problem(*case))

    make_output_file(out_filename, test_cases, solutions)


def make_output_file(out_filename, test_cases, solutions):
    f = open(out_filename, 'w')

    for i in range(test_cases):
        f.write("Case #%d: %d\n" % (i + 1, solutions[i]))

    f.close()


solve('A-small-attempt0.in', 'output_small.out')
solve('A-large.in', 'output_large.out')
