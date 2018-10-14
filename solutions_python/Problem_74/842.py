T = int(raw_input())

for t in xrange(T):
    line = raw_input().split()
    N = int(line[0])
    time = 0
    Opos = 1
    Otime = 0
    Bpos = 1
    Btime = 0
    for n in xrange(N):
        robot = line[2 * n + 1]
        pos = int(line[2 * n + 2])
        if robot == "O":
            if abs(pos - Opos) < time - Otime:
                time += 1
            else:
                time = Otime + abs(pos - Opos) + 1
            Opos = pos
            Otime = time
        elif robot == "B":
            if abs(pos - Bpos) < time - Btime:
                time += 1
            else:
                time = Btime + abs(pos - Bpos) + 1
            Bpos = pos
            Btime = time
    print "Case #%i: %i" % (t + 1, time)