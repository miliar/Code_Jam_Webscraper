nCases = eval(input())

for caseNum in range(nCases):

    firstAns = eval(input()) - 1
    firstTable = []
    for row in range(4):
        firstTable.append([int(x) for x in input().split()])

    secondAns = eval(input()) - 1
    secondTable = []
    for row in range(4):
        secondTable.append([int(x) for x in input().split()])

    print('Case #{}: '.format(caseNum + 1), end='')

    firstCandidates = firstTable[firstAns]
    secondCandidates = secondTable[secondAns]

    finalCandidates = set.intersection(set(firstCandidates), set(secondCandidates))
    result = len(finalCandidates)

    if (result == 1):
        for n in finalCandidates:
            print(n)
    elif (result > 1):
        print('Bad magician!')
    else:
        print('Volunteer cheated!')
