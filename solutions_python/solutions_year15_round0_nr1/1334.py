filename = "A-large.in"

f = open(filename, "r")
numTestCases = f.readline()

for testCase in range(int(numTestCases)):
    case = f.readline() # 111 111111
    maxShyness = case.split()[0]
    audience = case.split()[1]

    audienceByShyness = list(audience) # still strings
    currentStanding = 0

    audiencePlanted = 0

    for shyness in range(int(maxShyness) + 1):
        current = int(audienceByShyness[shyness])
        # print "shyness: " + str(shyness)
        if currentStanding >= shyness:
            currentStanding += current
            # print currentStanding
        elif current > 0:
            added = shyness - currentStanding
            # print "added: " + str(added)
            audiencePlanted += added
            currentStanding += current + added

    print "Case #" + str(testCase + 1) + ": " + str(audiencePlanted)