def solutionCheck(pancakes):
    for pancake in pancakes:
        if (pancake == "-"):
            return False;
    return True;

def flipperCheck(pancakes, flipper):
    flipsCount = 0
    pancakesSz = len(pancakes)
    for i in range(pancakesSz):
        if (pancakes[i] != "+"):
            try:
                flip(pancakes, i, i + flipper - 1)
            except:
                return "IMPOSSIBLE"
            flipsCount += 1
    if solutionCheck(pancakes)==False:
        return "IMPOSSIBLE"
    return flipsCount

def flip(pancakes, flipBegin, flipEnd):
    for i in range(flipBegin, flipEnd + 1):
        if (pancakes[i] == "+"):
            pancakes[i] = "-"
        else:
            pancakes[i] = "+"
    return pancakes


fSolution = open("solution.txt", "w")
fInput = open("large.txt", "r")
t = fInput.readline()
lineCount = 0
for line in fInput.readlines():
    pancakes, flipper = line.split(" ")
    flipsCount = flipperCheck(list(pancakes), int(flipper))
    lineCount += 1
    fSolution.write('Case #{}: {}\n'.format(lineCount, flipsCount))
fSolution.close()