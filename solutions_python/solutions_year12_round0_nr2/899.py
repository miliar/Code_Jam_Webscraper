def parse_line(x):
    line = x.split()
    return line

def compute_googlers(x):
    numDancers = int(x[0])
    numSurprises = int(x[1])
    minScore = int(x[2])
    total = 0
    if (minScore == 0):
        return numDancers
    for i in range(3, numDancers+3):
        if (int(x[i]) == 0):
            pass
        elif (int(x[i]) >= (minScore*3)-2):
            total += 1
        elif ((int(x[i]) >= (minScore*3)-4) and (numSurprises > 0)):
            total += 1
            numSurprises -= 1
    return total

def main(filename):
    testCase = []
    testLine = ''
    f = open(filename, "r")
    a = open("output2.txt", "w")
    numTestCases = int(f.readline())
    for x in range(1, numTestCases+1):
        testLine = f.readline()
        testCase = parse_line(testLine)
        result = compute_googlers(testCase)
        a.write('Case #' + str(x) + ': ' + str(result) + '\n')
    f.close()
    a.close()

main("B-large.in")
