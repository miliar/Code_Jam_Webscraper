def getTime(cost, farm, goal, gain, time):
    while True:
        goalTime = goal / gain
        farmTime = cost / gain
        if goalTime <= farmTime + (goal / (gain + farm)):
            time += goalTime
            return time
        else:
            time += farmTime
            gain += farm

def cookieClicker():
    infile = open('B-large.in', 'r')
    outfile = open('answer.txt', 'w')
    checker = open('checker.txt', 'w')

    cases = int(infile.readline())

    for case in range(cases):
        cost, farm, goal = infile.readline().rstrip().split(" ")
        cost = float(cost)
        farm = float(farm)
        goal = float(goal)
        gain = 2.0
        time = 0.0

        time = getTime(cost, farm, goal, gain, time)
        if case != cases:
            outfile.write("Case #" + str(case+1) + ": " + str(time) + "\n")
        else:
            outfile.write("Case #" + str(case+1) + ": " + str(time))

cookieClicker()
        
