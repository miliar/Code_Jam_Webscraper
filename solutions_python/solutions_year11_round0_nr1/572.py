T = int(raw_input())

for t in range(T):
    line = raw_input().split(' ')
    N = int(line.pop(0))

    pos = {'O': 1, 'B': 1}
    acc = 0
    last_robot = None
    move = 0

    for n in range(N):
        robot = line.pop(0)
        button = int(line.pop(0))
        step = abs(pos[robot] - button) + 1
        pos[robot] = button

        if robot != last_robot:
            move += acc
            acc = max(1, step - acc)
            last_robot = robot
        else:
            acc += step

    print "Case #%d: %d" % (t+1, move + acc)
