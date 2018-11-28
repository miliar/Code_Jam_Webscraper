def parse_input(filename, sep = '\n'):
    f = open(filename, 'r')
    ret = f.read().strip().split(sep)
    f.close()
    return ret

def write_output(filename, data):
    f = open(filename, 'w')
    caseNum = 1

    for answer in data:
        f.write("Case #" + str(caseNum) + ": " + str(answer) + "\n")
        caseNum += 1

def main():
    filenameIN = "A-large.in"
    filenameOUT = "results.out"

    inputData = parse_input(filenameIN)
    outputData = []

    inputData.remove(inputData[0])

    for testCase in inputData:
        testCase = testCase.split(" ")
        friends = 0
        shyLevel = 0
        peopleStanding = 0
        for group in testCase[1]:
            if peopleStanding >= shyLevel:
                peopleStanding += int(group)
            else:
                needed = shyLevel - peopleStanding
                friends += needed
                peopleStanding += needed
                peopleStanding += int(group)
            shyLevel += 1
        outputData.append(friends)

    write_output(filenameOUT, outputData)

if __name__ == "__main__":
    main()
