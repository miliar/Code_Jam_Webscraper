import re
import sys

"""
---+-++- 3  Case #1: 3
+++++ 4     Case #2: 0
-+-+- 4     Case #3: IMPOSSIBLE

"""


def solve_pancakes_1(line, k):
    """
    Solve the pancake problem in O(2^N) time
    :param line: the pancake line
    :param k: the width of the flipper
    :return: the number of -1 for impossible

    >>> solve_pancakes_1('---+-++-', 3)
    3
    >>> solve_pancakes_1('+++++', 4)
    0
    >>> solve_pancakes_1('-+-+-', 4)
    -1
    """
    lines = {line: 0}
    line_list = [line]

    for line in line_list:
        if line == '+' * len(line):
            return lines[line]

        moves = lines[line]
        for index, character in enumerate(line):
            if character == '-':
                # call flip to return new lines
                new_lines = flip(line, index, k)

                # check if the new lines are not in the lines made
                # if not added them and update the flags
                for new_line in new_lines:
                    if new_line not in line_list:
                        lines[new_line] = moves + 1
                        line_list.append(new_line)
                        if new_line == '+'*len(line):
                            return lines[new_line]

                        # new_line_added = True
    return -1

def flip(line, index, k):
    """
    return list of lines where all possible flips were made
    :param line: line of pancakes
    :param index: index of the center of the flip
    :param k: width of the flipper
    :return: list
    """

    new_lines = []

    for start in range(index - k, index + 1):
        if start >= 0 and start + k <= len(line):
            new_lines.append(get_new_line(line, start, k))

    return new_lines

def get_new_line(line, start, k):
    # flip from the start to start + k

    # check if there's before start
    new_line = line[:start]

    # flip
    # first case when the start is index
    for i in range(start, start + k):
        new_line += '-' if line[i] == '+' else '+'

        # add the rest of the cakes
    new_line += line[start + k:]

    return new_line

def main(file):
    f = open(file, 'r')

    first = True
    no_test_cases = 0
    test_cases = []
    for line in f:
        if first:
            no_test_cases = int(line)
            first = False
        else:
            test_case = re.split(" ", line)
            test_case[1] = test_case[1].strip()
            test_cases.append(test_case)

    for index, test_case in enumerate(test_cases):
        sol = solve_pancakes_1(test_case[0], int(test_case[1]))
        print("Case #{}: {}".format(index + 1,
                                    str(sol) if sol >= 0 else 'IMPOSSIBLE'))

    f.close()

if __name__ == '__main__':
    file_name = sys.argv[1]
    main(file_name)