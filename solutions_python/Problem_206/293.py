__author__ = 'Roberto'
import math

def finish(index, solution):

    print(solution)

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))
    debug_out.write("{0}\n".format( solution))

def solve_test(index, D, test_case):

    debug_out.write("Case #{0} In: {1} {2} Out: ".format(index, D, test_case))

    print("Case: [{0} {1}]".format(D, test_case))

    max_time = 0
    for horse in test_case:

        position, speed = map(int, horse.split())
        path = D - position
        time = path / speed
        if time > max_time:
            max_time = time

    finish(index, D / max_time)


if __name__ == "__main__":
    task = "A"
    level = 2
    attempts = 0

    if level == 0:
        file_name = "sample.in"
    elif level == 1:
        file_name = "{0}-small-attempt{1}.in".format(task, attempts)
    else:
        file_name = "{0}-large.in".format(task)



    file_out_name = file_name.replace("in", "out")
    file_out = open(file_out_name, 'w')
    debug_out = open(file_name.replace("in", "debug"), 'w')

    with open(file_name, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    number_of_lines = int(lines[0])

    test_cases = lines[1:]
    j = 0
    for i in range(0, number_of_lines):

        D, N = map(int, test_cases[j].split())
        j += 1
        solve_test(i, D, test_cases[j : j + N])
        j += N

    file_out.close()