def readlines(fileName):
    fh = open(fileName, "rb")
    return [line for line in fh]

def ezprint(results, outputFile):
    with open(outputFile, "wb") as fh:
        for i, result in enumerate(results):
            print >> fh, "Case #" + str(i+1) + ": " + result

def getnums(line):
    return [int(num) for num in line.split()]

def ezsort(sortable):
    return sorted(sortable, key=lambda x: x)

results = []

lines = readlines('A.txt') #Name of input file
numTestCases = int(lines[0])

for i in range(0,numTestCases):
    firstAnswer = int(lines[10*i+1])
    c1 = lines[10*i+2:10*i+6]
    secondAnswer = int(lines[10*i+6])
    c2 = lines[10*i+7:10*i+11]
    r1 = c1[firstAnswer-1].split()
    r2 = c2[secondAnswer-1].split()
    solution = 'Volunteer cheated!'
    for char in r1:
        if char in r2:
            if solution == 'Volunteer cheated!':
                solution = char
            else:
                solution = 'Bad magician!'
    results.append(solution)

ezprint(results, 'output.txt')