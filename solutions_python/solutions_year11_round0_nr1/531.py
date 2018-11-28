import fileinput
import itertools

def solve(bb):
    seconds_count = {'O': 0, 'B': 0}
    robot_position = {'O': 1, 'B': 1}
    last_robot = ''
    for robot, button in bb:
        seconds_count[robot] += abs(robot_position[robot]-button)
        robot_position[robot] = button
        if last_robot != robot:
            seconds_count[robot] = max(seconds_count['O'], seconds_count['B'])
        seconds_count[robot] += 1
        last_robot = robot
    return max(seconds_count.values())

readline = fileinput.input().readline
case_count = int(readline())
for case_no in range(case_count):
    button_list = readline().split()
    buttons = zip(button_list[1::2], [int(i) for i in button_list[2::2]])
    answer = solve(buttons)
    print "Case #%d: %s" % (case_no+1, answer)
