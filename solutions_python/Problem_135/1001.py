#!/usr/bin/env python

import sys


def read_line(file_path):
    for line in open(file_path, 'r').readlines():
        if line.strip():
            yield line.strip("\n")


def get_answer(generator):
    return int(generator.next())


def get_case_line(generator):
    i = 1
    answer = get_answer(generator)
    while i <= 4:
        if i == answer:
            line = [int(nbr) for nbr in str(generator.next()).split(' ')]
        else:
            generator.next()
        i += 1
    return answer, line


def lines_intersection(answer1, answer2):
    intersection = tuple(set(answer1).intersection(answer2))
    return intersection


def get_game_result(intersection):
    if not intersection:
        return "Volunteer cheated!"
    elif len(intersection) == 1:
        return intersection[0]
    else:
        return "Bad magician!"

if __name__ == '__main__':
    file_content = read_line(sys.argv[1])
    test_case_number = get_answer(file_content)
    current_case = 1

    while current_case <= test_case_number:
        answer1, line1 = get_case_line(file_content)
        answer2, line2 = get_case_line(file_content)
        intersection = lines_intersection(line1, line2)
        result_message = get_game_result(intersection)
        print("Case #{0}: {1}".format(current_case, result_message))
        current_case += 1

