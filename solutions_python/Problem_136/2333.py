with open('input.txt') as inputFile:
    tests = int(inputFile.readline())

    n = tests
    answers = []
    while tests:
        c, f, x = map(float, inputFile.readline().split())
        cps = 2.0
        time = 0.0
        timeforFarm = c / cps
        while time + timeforFarm + (x / (cps+f)) < time + (x / cps):
            time += timeforFarm
            cps += f
            timeforFarm = c / cps
        time += x / cps
        answers.append(time)
        tests -= 1

    with open('output.txt', 'w') as f:
        for i in xrange(1, n+1):
            f.write("Case #" + str(i) + ": " + str(answers[i-1]) + "\n")
