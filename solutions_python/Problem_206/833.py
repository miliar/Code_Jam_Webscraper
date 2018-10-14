def readFile(filename):
    result = []
    with open(filename) as file:
        for line in file:
            s = line.strip()
            result.append(s)
    return result

def solve(goal, horses):
    # Have to figure out the slowest horse time and just average that
    # Check each horse's finish time independently; they don't depend on eachother in truth
    slowestTime = 0
    for horse in horses:
        distRemain = horse[0]
        speed = horse[1]
        calcTime = (goal - distRemain) / speed
        slowestTime = max(slowestTime, calcTime)
    return goal / slowestTime

def q1():
    counter = 0
    states = readFile("BIG1in.txt")
    states = states[1:]
    grid = []
    i = 0
    mode = 0
    count = 1
    while i < len(states):
        goal = -1
        goal = int(states[i].split()[0])
        numHorse = int(states[i].split()[1])
        horses = []
        for j in range(numHorse):
            i += 1
            horses.append([int(x) for x in states[i].split()])
        print("Case #" + str(count) + ": " + str(solve(goal, horses)))
        i += 1
        count += 1
q1()
