T = int(raw_input())
for t in xrange(T):
    chars = raw_input().split(' ')[1:]
    buttons = []
    for i in xrange(0, len(chars), 2):
        buttons.append((chars[i], int(chars[i + 1])))
    #print buttons

    robot_o = 1
    robot_b = 1
    time = 0

    for i, v in enumerate(buttons):
        robot, button = v
        if robot == 'O':
            while True:
                #print "O: %d, %d" % (robot_o, robot_b)
                for robot2, btn2 in buttons[i+1:]:
                    if robot2 == 'B':
                        if robot_b < btn2:
                            robot_b += 1
                        elif robot_b > btn2:
                            robot_b -= 1
                        break
                time += 1
                if button == robot_o:
                    break
                if robot_o < button:
                    robot_o += 1
                else:
                    robot_o -= 1
        else:
            while True:
                #print "B: %d, %d" % (robot_o, robot_b)
                for robot2, btn2 in buttons[i+1:]:
                    if robot2 == 'O':
                        if robot_o < btn2:
                            robot_o += 1
                        elif robot_o > btn2:
                            robot_o -= 1
                        break
                time += 1
                if button == robot_b:
                    break
                if robot_b < button:
                    robot_b += 1
                else:
                    robot_b -= 1
    print "Case #%d: %d" % (t + 1, time)

