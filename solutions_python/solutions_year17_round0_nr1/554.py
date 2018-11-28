inputFile = open("resources/A-large.in", "r")
outputFile = open("resources/A-large.out", "w")


def isImpossible(pancakes, diff):
    for i in range(diff, len(pancakes) - diff - 1):
        if pancakes[i] != pancakes[i + 1]:
            return True
    return False


T = int(inputFile.readline())

for t in range(1, T + 1):
    l = inputFile.readline().split(' ')
    pancakes = (l[0])
    k = int(l[1])

    if len(pancakes) % 2 == 0:
        if k >= 0.5 * (len(pancakes) + 2):
            if isImpossible(pancakes, len(pancakes) - k):
                outputFile.write("Case #" + str(t) + ": IMPOSSIBLE" + "\n")
                continue
    else:
        if k > 0.5 * (len(pancakes) + 1):
            if isImpossible(pancakes, len(pancakes) - k):
                outputFile.write("Case #" + str(t) + ": IMPOSSIBLE" + "\n")
                continue

    flips = 0
    pancakesList = list(pancakes)
    for i in range(0, len(pancakes) - k + 1):
        if pancakesList[i] == '-':
            for j in range(i, i + k):
                if pancakesList[j] == '-':
                    pancakesList[j] = '+'
                else:
                    pancakesList[j] = '-'
            flips += 1

    if '-' in pancakesList:
        outputFile.write("Case #" + str(t) + ": IMPOSSIBLE" + "\n")
        continue

    outputFile.write("Case #" + str(t) + ": " + str(flips) + "\n")
