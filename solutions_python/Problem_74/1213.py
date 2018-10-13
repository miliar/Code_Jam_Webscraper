#!/usr/bin/env python
import sys

if __name__ == '__main__':
    input_lines = [line.rstrip() for line in open(sys.argv[1] + ".in", "r").readlines()]
    output_file = open(sys.argv[1] + ".out", "w")

    num_test_cases = int(input_lines[0])
    test_cases = input_lines[1:]

    for test_num in xrange(len(test_cases)):
        test_case = test_cases[test_num].split(" ")

        num_buttons = int(test_case.pop(0))
        queues = {'B':[], 'O':[]}
        last_robot = None
        positions = {'B':1, 'O':1}
        # queue item format: (action, prerequisite from other)
        for button_num in xrange(num_buttons):
            robot = test_case.pop(0)
            target_button = int(test_case.pop(0))
            if last_robot != robot and last_robot is not None:
                button_prerequisite = queues[last_robot][-1][0]
            else:
                button_prerequisite = None
            if target_button > positions[robot]:
                queues[robot] += [(('move', pos), None) for pos in range(positions[robot]+1, target_button+1)]
            elif target_button < positions[robot]:
                queues[robot] += [(('move', pos), None) for pos in range(positions[robot]-1, target_button-1, -1)]
            positions[robot] = target_button
            queues[robot].append((('press', target_button), button_prerequisite))
            last_robot = robot

        actions_done = {'B':[], 'O':[]}
        moves = 0
        while len(queues['B'] + queues['O']) > 0:
            press_made = False  # avoid simultaneous presses
            if len(queues['B']) > 0:
                B_next_action = queues['B'][0]
                if B_next_action[1] is None or B_next_action[1] in actions_done['O']:  # if no prerequisite, or O already did the prerequisite
                    actions_done['B'].append(queues['B'].pop(0)[0])
                    if B_next_action[0][0] == 'press':
                        press_made = True
            if len(queues['O']) > 0:
                O_next_action = queues['O'][0]
                if O_next_action[1] is None or O_next_action[1] in actions_done['B']:  # same, but the other way round
                    if O_next_action[0][0] != 'press' or not press_made:
                        actions_done['O'].append(queues['O'].pop(0)[0])
            moves += 1

        output_file.write("Case #{casenum}: {moves_taken}\n".format(casenum=test_num+1, moves_taken=moves))
        print "Case #{casenum}: {moves_taken}".format(casenum=test_num+1, moves_taken=moves)
    
    output_file.close()
