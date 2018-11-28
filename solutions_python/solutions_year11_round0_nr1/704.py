
def run(steps):
    steps = steps.split(" ")
    steps = [(steps[i], int(steps[i + 1])) for i in xrange(0, len(steps), 2)]
    last_pos = {"O": 1, "B": 1}
    secs = incr = 0
    last_robot = steps[0][0]
    for robot, pos in steps:
        diff = abs(last_pos[robot] - pos)
        # if robots are different, we need to consider the current robot could
        # be walking together with the previous one
        if last_robot != robot:
            secs += incr
            if diff <= incr:
                incr = 1
            else:
                incr = 1 + diff - incr
        else:
            incr += diff + 1
        last_robot = robot
        last_pos[robot] = pos
    secs += incr
    return secs

if __name__ == "__main__":
    for i in range(int(raw_input())):
        test_case = raw_input()
        n_buttons, steps = test_case.split(" ", 1)
        print "Case #%d: %d" % (i + 1, run(steps))
