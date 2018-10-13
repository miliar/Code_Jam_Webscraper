import sys


def remainingTime(prod, x, current):
    return (x - current) * 1.0 / prod


def questionB(cost, farmProduction, goal):
    time = 0.0
    cookies = 0
    production = 2.0

    while True:
        timeToGoal = remainingTime(production, goal, cookies)
        timeToFactory = remainingTime(production, cost, cookies)

        comparisonTime = time + timeToFactory + remainingTime(production+farmProduction,
                                                              goal,
                                                              cookies)

        if comparisonTime < timeToGoal + time:
            time += timeToFactory
            production += farmProduction
        else:
            time += timeToGoal
            break
    return time


if __name__ == '__main__':
    filename = sys.argv[1]
    text = open(filename, "r").readlines()
    testcases = int(text[0])
    text = text[1:]

    for index, line in enumerate(text):
        text[index] = line.replace('\n', '')

    outfile = open("out.txt", "a")

    for i in range(testcases):
        cost, production, goal = text[0].split(' ')

        time = questionB(float(cost), float(production), float(goal))

        result = "Case #%d: %f\n" % (int(i) + 1, time)
        outfile.write(result)

        text = text[1:]
