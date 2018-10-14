import sys


if __name__ == "__main__":

    f = open(sys.argv[1])
    testcount = int(f.readline())

    for testindex in range(0, testcount):

        line = f.readline()
        vals = line.strip().split()

        n = int(vals[0])
        del vals[0]

        robots = []
        positions = []
        for i in range(0, n):
            robots.append(vals[i*2])
            positions.append(int(vals[i*2+1]))

        o_pos = 1
        b_pos = 1
        last_o_push_time = 0
        last_b_push_time = 0
        for robot, pos in zip(robots, positions):
            if robot == 'O':
                last_o_push_time += abs(o_pos-pos) + 1
                if last_o_push_time <= last_b_push_time:
                    last_o_push_time = last_b_push_time + 1
                o_pos = pos
            if robot == 'B':
                last_b_push_time += abs(b_pos-pos) + 1
                if last_b_push_time <= last_o_push_time:
                    last_b_push_time = last_o_push_time + 1
                b_pos = pos

        print "Case #%i: %i" % (testindex+1, max(last_o_push_time, last_b_push_time))
