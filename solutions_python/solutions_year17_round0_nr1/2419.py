# GET FILE #
cases = [line.split() for line in open("A-large.in").readlines()[1:]]
outputFile = open("A.out","w")
caseCount = 1
# FOR EACH CASE #
for case in cases:
    pancakes = [char for char in case[0]]
    flipper = int(case[1])
    flipCount = 0
    while "-" in pancakes:
        startFlip = pancakes.index("-")
        if len(pancakes[startFlip:]) < flipper:
            break
        else:
            currentPancake = 0
            for pancake in pancakes[startFlip:startFlip+flipper]:
                if pancake == "+":
                    pancakes[startFlip+currentPancake] = "-"
                else:
                    pancakes[startFlip + currentPancake] = "+"
                currentPancake += 1
            flipCount += 1

    if "-" in pancakes:
        outputFile.write("Case #" + str(caseCount) + ": IMPOSSIBLE\n")
    else:
        outputFile.write("Case #" + str(caseCount) + ": " + str(flipCount) + "\n")
    caseCount += 1
outputFile.close()