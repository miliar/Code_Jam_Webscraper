import math

def getCases(filename):
    inputFile = open(filename)
    cases = readInput(inputFile)
    inputFile.close()
    return cases

def readInput(inputFile):
    lines = int(inputFile.readline())
    cases = []
    for _ in range(lines):
        line = inputFile.readline().strip()
        values = line.split(' ')
        case = {'N': int(values[0]), 'S': int(values[1]), 'p': int(values[2]), 
                'totals': [int(x) for x in values[3:]]}
        cases.append(case)
    return cases

def maxLimit(total):
    avg = total / 3.0
    return min(int(math.ceil(avg)) + 6, 30)

def maxScoreWithoutSuprise(total):
    for x in range(maxLimit(total), 0, -1):
        if (total - x >= 2 * max(x - 1, 0)): return x
    return 0

def maxScoreWithSuprise(total):
    for x in range(maxLimit(total), 0, -1):
        if (total - x >= 2 * max(x - 2, 0)): return x
    return 0

def solveProblem(cases):
    result = []
    for case in cases:
        result.append(solveCase(case))
    return result

def solveCase(case):
    suprises = case['S']
    p = case['p']
    result = 0
    for idx in range(case['N']):
        total = case['totals'][idx]
        if maxScoreWithoutSuprise(total) >= p:
            result += 1
        elif suprises > 0 and maxScoreWithSuprise(total) >= p:
            result += 1
            suprises -= 1
    return result

def outputResults(results):
    outputFile = open('B-large.out', 'w')
    for idx in range(len(results)):
        result = 'Case #%d: %d\n' % (idx + 1, results[idx])
        outputFile.write(result)
    outputFile.close()
    
if __name__ == '__main__':
    cases = getCases('B-large.in')
    results = solveProblem(cases)
    outputResults(results)