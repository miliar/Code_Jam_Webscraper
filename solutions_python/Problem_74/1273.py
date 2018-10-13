f = open("A-large.in")

T = int(f.readline())
nf = open("A-large.out", "w")

for case in range(T):
    line = f.readline()
    x = line.split()[1:]
    tasks = []
    bits = []

    goals = [[], []]
    
    for i in range(0, len(x)-1, 2):
        tasks.append(int(x[i+1]))

        if x[i] == "B":
            bits.append(1)
            goals[1].append(int(x[i+1]))

        else:
            bits.append(0)
            goals[0].append(int(x[i+1]))

    time = 0
    pos = [1, 1]
    indii = [0, 0]
    hdone = 0

    for i in range(len(tasks)):
        x = bits[i]

        t = abs(tasks[i] - pos[x]) + 1
        pos[x] = tasks[i]
        indii[x] += 1

        if indii[1-x] == len(goals[1-x]):     # one robot has finished tasks
            hdone = 1

        if not hdone:                    # move other robot
            othergoal = goals[1-x][indii[1-x]]

            if abs(pos[1-x] - othergoal) < t:
                pos[1-x] = othergoal

            else:
                pos[1-x] = othergoal + abs(pos[1-x] - othergoal) - t


        time += t
        
    nf.write("Case #%d: %d\n" % (case+1, time))


nf.close()

        
        


        