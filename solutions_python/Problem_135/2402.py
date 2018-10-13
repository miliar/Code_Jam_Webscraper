with open('input.txt') as f:
    tests = int(f.readline())

    n = tests
    answers = []
    while tests:
        first = int(f.readline())
        firstArrangement = []
        for _ in xrange(4):
            firstArrangement.append(map(int, f.readline().split()))
        second = int(f.readline())
        secondArrangement = []
        for _ in xrange(4):
            secondArrangement.append(map(int, f.readline().split()))
        firstRow = set(firstArrangement[first - 1])
        secondRow = set(secondArrangement[second - 1])
        intersect = firstRow.intersection(secondRow)
        if len(intersect) == 0:
            answers.append("Volunteer cheated!")
        elif len(intersect) == 1:
            answers.append(list(intersect)[0])
        else:
            answers.append("Bad magician!")

        tests -= 1

    with open('output.txt', 'w') as f:
        for i in xrange(1, n+1):
            f.write("Case #" + str(i) + ": " + str(answers[i-1]) + "\n")
