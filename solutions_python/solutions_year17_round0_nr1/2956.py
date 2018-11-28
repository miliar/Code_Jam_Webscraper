import fileinput

pastFirstLine = False
caseNum = 0

for line in fileinput.input():
    if pastFirstLine:
        strings = line.split()
        pancakes = list(strings[0])
        flipper = int(strings[1])
        i = 0
        flips = 0

        while i + flipper <= len(pancakes):
            if pancakes[i] == "-":
                flips += 1
                j = 0

                while j <= flipper - 1:
                    if pancakes[i + j] == "-":
                        pancakes[i + j] = "+"
                    else:
                        pancakes[i + j] = "-"
                    j += 1
            i += 1
        caseNum += 1

        if "-" in pancakes:
            print "Case #" + str(caseNum) + ": " + "IMPOSSIBLE"
        else:
            print "Case #" + str(caseNum) + ": " + str(flips)
    else:
        pastFirstLine = True
