def cookieCalculator(C, F, X):
    rate = 2
    time = 0.0
    isGoalReached = False

    while not isGoalReached:
        timeToGoal = X / rate
        timeToFarmThenGoal = (C / rate) + (X / (rate + F))

        if timeToGoal < timeToFarmThenGoal:
            time += timeToGoal
            isGoalReached = True
        else:
            time += C / rate
            rate += F

    return time

f = open('B-large.in', 'r')
o = open('B-large.out', 'w')

T = int(f.readline())

for t in range(T):
    line = f.readline().replace('\n', ' ').split(' ')

    C = float(line[0])
    F = float(line[1])
    X = float(line[2])

    o.write('Case #%d: %.7f\n' % (t+1, cookieCalculator(C, F, X)))