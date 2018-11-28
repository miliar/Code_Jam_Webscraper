import re

f = open('A-large.in', 'r')
# f = open('A-bot-trust.in', 'r')

numofcases = f.readline()

for i in range(int(numofcases)):
    line = f.readline()
    buttons = []
    robot_o = []
    robot_b = []
    cases = re.findall("([O|B]) (\d+)", line)
    for case, button in cases:
        if case == 'B':
            robot_b.append(int(button))
        elif case == 'O':
            robot_o.append(int(button))
        buttons.append(case + button)

    pos_robot_o = pos_robot_b = 1
    seconds = 0
    # print buttons
    while len(buttons) > 0:
        button = buttons.pop(0)
        robot = button[0]
        if robot == 'O':
            time_robot_o = abs(robot_o[0] - pos_robot_o) + 1
            seconds += time_robot_o
            pos_robot_o = robot_o[0]
            robot_o.pop(0)
            if len(robot_b) > 0:
                if pos_robot_b < robot_b[0]:
                    pos_robot_b += time_robot_o
                    if pos_robot_b > robot_b[0]:
                        pos_robot_b = robot_b[0]
                elif pos_robot_b > robot_b[0]:
                    pos_robot_b -= time_robot_o
                    if pos_robot_b < robot_b[0]:
                        pos_robot_b = robot_b[0]
        elif robot == 'B':
            time_robot_b = abs(robot_b[0] - pos_robot_b) + 1
            seconds += time_robot_b
            pos_robot_b = robot_b[0]
            robot_b.pop(0)
            if len(robot_o) > 0:
                if pos_robot_o < robot_o[0]:
                    pos_robot_o += time_robot_b
                    if pos_robot_o > robot_o[0]:
                        pos_robot_o = robot_o[0]
                elif pos_robot_o > robot_o[0]:
                    pos_robot_o -= time_robot_b
                    if pos_robot_o < robot_o[0]:
                        pos_robot_o = robot_o[0]
        # print "--- %d : %s : B%d : O%d" % (seconds, robot, pos_robot_b, pos_robot_o)
    print "Case #%d: %d" % (i+1, seconds)
f.close()