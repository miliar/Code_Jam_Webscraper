#!/usr/bin/env python

SIZE = 4

def run_one(choice1, layout1, choice2, layout2):
    set1 = set(layout1[choice1 - 1])
    set2 = set(layout2[choice2 - 1])

    union = set1 & set2

    if len(union) == 1:
        return union.pop()
    elif len(union) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # First choice and layout
        choice1 = int(lines.popleft())
        layout1 = [[int(cell) for cell in lines.popleft().rstrip('\r\n').split(' ')] for row in range(SIZE)]

        # Second choice and layout
        choice2 = int(lines.popleft())
        layout2 = [[int(cell) for cell in lines.popleft().rstrip('\r\n').split(' ')] for row in range(SIZE)]

        result = run_one(choice1, layout1, choice2, layout2)

        output.append('Case #{0}: {1}'.format(t + 1, result))

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque(file.readlines())
        output = run(lines)
        print os.linesep.join(output)
