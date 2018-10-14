import sys

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    pos_O = pos_B = 1
    time_O = time_B = 0

    line = f.readline().split()
    N = line[0]
    for i in range(1, len(line), 2):
        color = line[i]
        pos = int(line[i+1])
        time = 0
        if color == "O":
            time = abs(pos_O - pos) + 1
            time_O += time
            if time_O < time_B + 1: time_O = time_B + 1
            pos_O = pos
        else:
            time = abs(pos_B - pos) + 1
            time_B += time
            if time_B < time_O + 1: time_B = time_O + 1
            pos_B = pos
    print "Case #%d: %d" % (case + 1, max(time_O, time_B))
