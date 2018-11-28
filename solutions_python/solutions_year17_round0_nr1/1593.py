def getInvertedChar(char):
    if char == '+':
        return '-'
    return '+'


def solve(S, K):

    pancakes = list(S)

    i = 0
    flipCount = 0
    while i <= len(pancakes) - K:
        if pancakes[i] == '+':
            i += 1
            continue;

        flipCount += 1

        j = 0
        while j < K:
            pancakes[i + j] = getInvertedChar(pancakes[i + j])
            j += 1
        i += 1

    i = 0
    while i < len(pancakes):
        if pancakes[i] == '-':
            return 'IMPOSSIBLE'
        i += 1

    return flipCount

#inputFile = open('A-small-attempt0.in', 'r')
#outputFile = open('A-small-attempt0.out', 'w')

inputFile = open('A-large.in', 'r')
outputFile = open('A-large.out', 'w')

testCase = int(inputFile.readline())
for case in range(1, testCase + 1):
    parts = inputFile.readline().split()
    S = parts[0]
    K = int(parts[1])
    outputFile.write('Case #{}: {}\n'.format(case, solve(S, K)))

inputFile.close()
outputFile.close()
