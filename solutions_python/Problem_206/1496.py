import math

with open("A-large.in") as f:
    T = int(f.readline())

    for test in range(T):
        D, N = [int(e) for e in f.readline().split(" ")]

        positions = {}
        positions[D] = 0

        for n in range(N):
            pos, speed = [int(e) for e in f.readline().split(" ")]
            if not pos in positions.keys():
                positions[pos] = speed
            else:
                positions[pos] = min(speed, positions[pos])

        TIME = 0

        while len(positions) > 1:
            nexttime = -1
            oldpos = [(k, v) for k, v in positions.items()]
            positions = {}
            positions[D] = 0

            oldpos = sorted(oldpos)
            # print(oldpos)
            for i in range(len(oldpos) - 1):
                for j in [i + 1]:
                    # print(i, j)
                    if oldpos[i][1] != oldpos[j][1]:
                        newtime = (oldpos[j][0] - oldpos[i]
                                   [0]) / (oldpos[i][1] - oldpos[j][1])
                        if newtime > 0:
                            # newtime = math.ceil(newtime)
                            if nexttime == -1:
                                nexttime = newtime
                            else:
                                nexttime = min(nexttime, newtime)

            if nexttime == -1:
                break

            TIME += nexttime
            for pos, s in oldpos:
                pos += s * nexttime
                if pos <= D:
                    if not pos in positions.keys():
                        positions[pos] = s
                    else:
                        positions[pos] = min(s, positions[pos])

        # oldpos = [(k, v) for k, v in positions.items()]
        # if oldpos[0]
        # TIME += oldpos[0]

        print("Case #{0}: {1}".format(test + 1, D / TIME))
