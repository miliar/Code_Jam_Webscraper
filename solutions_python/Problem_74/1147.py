#!/usr/bin/env python2

# Google Code Jam 2011 - Problem A. Bot Trust
# David Jennings <dtkjennings@gmail.com>

import sys

def main():
    data = sys.stdin.readlines()
    case = 1

    # loop through lines to read test cases
    for i in range(int(data[0])):
        arr = data[case].strip().split()
        completeTestCase(case, arr)
        case += 1


def completeTestCase(case, test_list):
    master_sequence = []
    orange_buttons = []
    blue_buttons = []
    orange_position = 1;
    blue_position = 1;
    line_index = 1;
    # loop through pairs of robot and button numbers
    for a in range(int(test_list[0])):
        robot = test_list[line_index]
        button = int(test_list[line_index + 1])
        if robot == 'O':
            orange_buttons.append(button)
        elif robot == 'B':
            blue_buttons.append(button)
        else:
            print 'INVALID ROBOT!!'
            break

        master_sequence.append(robot + str(button));
        line_index += 2

    time_count = 0;
    # loop while the master sequence still has entries
    while len(master_sequence) > 0:
        orange_moved = False
        blue_moved = False

        # evaluate orange move
        if len(orange_buttons) > 0:
            if orange_buttons[0] > orange_position:
                orange_position += 1
                orange_moved = True
            elif orange_buttons[0] < orange_position:
                orange_position -= 1
                orange_moved = True

        # evaluate blue move
        if len(blue_buttons) > 0:
            if blue_buttons[0] > blue_position:
                blue_position += 1
                blue_moved = True
            elif blue_buttons[0] < blue_position:
                blue_position -= 1
                blue_moved = True

        # evaluating button press (only one per round)
        if master_sequence[0][0] == 'O':
            if int(master_sequence[0][1:]) == orange_position and not orange_moved:
                del orange_buttons[0] # popleft
                del master_sequence[0] # popleft
        elif master_sequence[0][0] == 'B':
            if int(master_sequence[0][1:]) == blue_position and not blue_moved:
                del blue_buttons[0] # popleft
                del master_sequence[0] # popleft

        time_count += 1;

    print 'Case #'+ str(case) + ':', time_count


if __name__ == '__main__':
    main()
