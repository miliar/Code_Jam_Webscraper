#!/usr/bin/python

import string
import sys


def solve(input, output):
    # loop through cases
    for i in range(int(input.readline())):
        total_steps = 0
        case = input.readline().split(' ')
        target_count = int(case.pop(0))
        prev_step = 0
        prev_robot = case[0]
        cur_pos = {'O': 1, 'B': 1}
        # loop of individual targets
        for j in range(target_count):
            print ' move %s %s' % (case[j*2], case[j*2+1])
            cur_robot = case[j*2]
            target = int(case[j*2+1])
            cur_step = abs(target - cur_pos[cur_robot]) + 1
            cur_pos[cur_robot] = target
            # add more credits if robot is the same
            if prev_robot == cur_robot:
                prev_step += cur_step
            # get credits if previous robot is different
            else:
                # calc effective step
                cur_step = max(cur_step - prev_step, 1)
                # initialize next round
                prev_step = cur_step
                prev_robot = cur_robot

            # add to total
            total_steps += cur_step
            print ' added %d, total_step is now %d' % \
                (cur_step, total_steps)

        print 'Case #%d: %d' % (i+1,total_steps)
        output.write('Case #%d: %d\n' % (i+1,total_steps))

def main():
    in_file = sys.argv[1]
    input = open(in_file)
    output = open(in_file + '.result', 'w')

    solve(input, output)

    input.close()
    output.close()

if __name__ == '__main__':
    main()
