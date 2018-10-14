__author__ = 'Roberto'
import math



def finish(index, solution):

    print solution

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))
    debug_out.write("{0}\n".format( solution))

def solve_test(index, test_case):

    debug_out.write("Case #{0} In: {1} Out:".format(index, test_case))

    print "Case: [{0}]".format(test_case)

    number = test_case
    if len(number) == 1:
        finish(index, number)
        return

    result = []

    repeat = 1
    for i in xrange(len(number)):

        if i == len(number) - 1:
            result.extend([number[i]] * repeat)
            break

        if number[i] == number[i + 1]:
            repeat += 1

        elif number[i] < number[i + 1]:
            result.extend([number[i]] * repeat)
            repeat = 1

        else:
            result.append(chr(ord(number[i]) - 1))
            result.extend(["9"] * (len(number) - len(result)))
            break

    i = 0
    while i < len(result) and result[i] == '0':
        i += 1

    final_result = "".join(result[i:])

    finish(index, final_result)


if __name__ == "__main__":
    task = "B"
    level = 2
    attempts = 1

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

    for i in xrange(0, number_of_lines):

        solve_test(i, test_cases[i])

    file_out.close()