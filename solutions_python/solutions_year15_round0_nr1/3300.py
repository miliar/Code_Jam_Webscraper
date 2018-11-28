def readFile(filename):
    f = open(filename, 'r')
    totalCases = int(f.readline()[:-1])
    cases = []
    for _ in range(totalCases):
        case = []
        line = f.readline()
        if '\n' in line:
            line = line[:-1]
        cases.append(line.split(' '))
    f.close()
    return cases

def ovation(maxShyness, audience):
    audienceOvated = 0
    audienceGroups = [int(i) for i in str(audience)]
    audienceNeeded = 0
    for shyLevel, newOvations in enumerate(audienceGroups):
        if audienceOvated + audienceNeeded < shyLevel:
            audienceNeeded += 1
        audienceOvated += newOvations
        if audienceOvated > maxShyness:
            break
    return audienceNeeded

def ovationScript(infile, outfile):
    cases = readFile(infile)
    output = []
    for index, case in enumerate(cases):
        maxShyness = int(case[0])
        audience = case[1]
        friendsNeeded = ovation(maxShyness, audience)
        output.append('Case #' + str(index + 1) + ": " + str(friendsNeeded))
    output = '\n'.join(output)
    f = open(outfile, 'w')
    f.write(output)
    f.close()

#infile = 'io/A-small-test.in'
#infile = 'io/A-small-attempt0.in'
infile = 'io/A-large.in'

#outfile = 'io/A-small-test.out'
#outfile = 'io/A-small-attempt0.out'
outfile = 'io/A-large.out'

ovationScript(infile, outfile)