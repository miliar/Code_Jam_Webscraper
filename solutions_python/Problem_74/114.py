N = int(input())

for num in range(1, N + 1):
    cmd = input().split()[1:]
    for i in range(len(cmd)):
        if cmd[i] == 'O':
            cmd[i] = 0
        elif cmd[i] == 'B':
            cmd[i] = 1
        else:
            cmd[i] = int(cmd[i])
    T = 0
    Coord = [1, 1]
    for step in range(0, len(cmd), 2):
        MainRobot = cmd[step]
        NewPos = cmd[step + 1]
        TimeStep = 1 + abs(Coord[MainRobot] - NewPos)
        Coord[MainRobot] = NewPos
        AnotherRobot = 1 - MainRobot
        j = step + 2
        while j < len(cmd) and cmd[j] != AnotherRobot:
            j += 2
        if j < len(cmd):
            NewPos = cmd[j + 1]
            if abs(NewPos - Coord[AnotherRobot]) <= TimeStep:
                Coord[AnotherRobot] = NewPos
            else:
                if NewPos > Coord[AnotherRobot]:
                    Coord[AnotherRobot] += TimeStep
                else:
                    Coord[AnotherRobot] -= TimeStep
        T += TimeStep
    print("Case #", num, ": ", T, sep = '')

