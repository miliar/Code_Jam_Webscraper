from sys import stdin, stdout



numCases = int(stdin.readline())

for case in range(0, numCases):
    order = []    
    line = stdin.readline().split()
    numActions = int(line[0])

    color = line[1]
    pos = int(line[2])

    if color == 'B':
        bluePos = pos
        orgPos = 1
    else:
        orgPos = pos
        bluePos = 1
    time = pos
    prevTime = time
    prevColor = color

    for action in range(2, numActions + 1):
        color = line[action * 2 - 1]
        pos = int(line[action * 2])
        if color == 'B':
            delta = abs(bluePos - pos)
            bluePos = pos
        else:
            delta = abs(orgPos - pos)
            orgPos = pos
        if prevColor == color:
            time += delta + 1
            prevTime += delta + 1
        elif delta > prevTime:
            delta -= prevTime
            time += delta + 1
            prevTime = delta + 1
        else:
            time += 1
            prevTime = 1

        prevColor = color

    print "Case #%s: %s" % (case + 1, time)

