import os


def solve_problem(coded_crowd):
    response = 0

    if len(coded_crowd) > 1:
        people_in_crowd = 0

        for shyness_level in xrange(1, len(coded_crowd)):
            number = int(coded_crowd[shyness_level - 1])
            people_in_crowd += number

            if people_in_crowd < shyness_level:
                needed_people = shyness_level - people_in_crowd
                response += needed_people
                people_in_crowd += needed_people

    return response


def exec_program(problem_folder, file_name):
    input_file_name = file_name + '.in'
    output_file_name = file_name + '.out'

    input_file = os.path.join(problem_folder, input_file_name)
    output_file = os.path.join(problem_folder, output_file_name)

    with open(input_file, 'rb') as in_file:
        with open(output_file, 'wb') as out_file:
            for index, line in enumerate(in_file):
                if index != 0:
                    splitted_line = line.split(' ')
                    response = solve_problem(splitted_line[1].replace('\r\n', ''))
                    out_file.write("Case #%d: %d\r\n" % (index, response))


exec_program(r'D:\Users\Daniel\Documents\Google Code Jam\Problem A', 'A-large')