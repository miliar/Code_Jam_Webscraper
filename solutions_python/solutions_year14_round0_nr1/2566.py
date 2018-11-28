__author__ = 'Maciej Jaworski'

import fileinput


def solve_set(first_answer, first_set, second_answer, second_set, case):
    answer = filter(lambda x: x in second_set[second_answer - 1],first_set[first_answer-1])

    if not answer:
        return 'Case #{}: Volunteer cheated!'.format(case)
    elif len(answer) == 1:
        return 'Case #{}: {}'.format(case, answer[0])
    else:
        return 'Case #{}: Bad Magician!'.format(case)


cnt = 0
case = 0
cases = 0

first_answer = None
first_set = []

second_answer = None
second_set = []

for line in fileinput.input():
    if line:
        if cnt == 0:
            cases = int(line)
        else:
            if (cnt - 1) % 10 == 0:
                first_answer = int(line)
            if (cnt - 1) % 10 in [1, 2, 3, 4]:
                first_set.append([int(x) for x in line.split(' ')])
            if (cnt - 1) % 10 == 5:
                second_answer = int(line)
            if (cnt - 1) % 10 in [6, 7, 8, 9]:
                second_set.append([int(x) for x in line.split(' ')])

            if len(second_set) == 4:
                case += 1
                print solve_set(first_answer, first_set, second_answer, second_set, case)
                first_answer = None
                first_set = []

                second_answer = None
                second_set = []

        cnt += 1
