def process_case(movs):
    robot = movs[0][0]
    other = {'O':'B', 'B':'O'}[robot]
    robotpos, otherpos = 1, 1
    movs_total = 0
    old_movs_total = 0
    
    robotmovs = 0
    othermovs = 0
    resto = 0

    for mov in movs:
        if robot != mov[0]: #cambio
            resto = movs_total - old_movs_total
            old_movs_total = movs_total
            other = robot
            robot = mov[0]
            robotpos, otherpos = otherpos, robotpos
            robotmovs, othermovs = othermovs, robotmovs
        
        #print("mov={}, robot={}, robotpos={}, robotmovs={}, other={}, otherpos={}, othermovs={}".format(mov, robot, robotpos, robotmovs, other, otherpos, othermovs))
        robotmovs = abs(mov[1] - robotpos) + 1 - resto
        resto = 0
        robotpos = mov[1]
        if robotmovs < 1:
            robotmovs = 1
        movs_total += robotmovs
        #print("mov={}, robot={}, robotpos={}, robotmovs={}, other={}, otherpos={}, othermovs={}".format(mov, robot, robotpos, robotmovs, other, otherpos, othermovs))
        #print()
    return movs_total

def run():
    f = open("in")

    testcases = int(f.readline())
    
    for case in range(testcases):
        line = f.readline()
        linesplit = line.split()
        nmovs = int(linesplit[0])
        movs = []
        for i in range(1, (2*nmovs)+1, 2):
            movs.append((linesplit[i], int(linesplit[i+1])))
        t = process_case(movs)
        print("Case #{}: {}".format(case+1, t))
    
    f.close()

if __name__ == "__main__":
    run()