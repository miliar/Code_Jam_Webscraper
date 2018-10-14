prefix = "A-small-attempt0"
postfixIn = ".in"
postfixOut = ".out"

fileIn = open(prefix + postfixIn, "r")
lines = fileIn.readlines()
fileIn.close()

results = []
template = "Case #%d: %s\n"

############################################################

msgBadMagician = "Bad magician!"
msgVolunteerCheated = "Volunteer cheated!"

casesCount = int(lines[0].strip())
linesPerCase = 10
for i in xrange(casesCount):
    firstLine = i * linesPerCase
    firstAnswer = int(lines[1 + firstLine].strip())
    firstRow = [int(elem) for elem in \
                lines[1 + firstAnswer + firstLine].strip().split()]
    secondAnswer = int(lines[6 + firstLine].strip())
    secondRow = [int(elem) for elem in \
                 lines[6 + secondAnswer + firstLine].strip().split()]
    magicianAnswer = 0
    message = ""
    for j in xrange(len(firstRow)):
        if firstRow[j] in secondRow:
            if magicianAnswer > 0:
                message = msgBadMagician
                break
            else:
                magicianAnswer = firstRow[j]
    if len(message) < 1:
        if magicianAnswer > 0:
            message = str(magicianAnswer)
        else:
            message = msgVolunteerCheated
    result = template % (i + 1, message)
    results.append(result)

############################################################

fileOut = open(prefix + postfixOut, "w")
for result in results:
    fileOut.write(result)
fileOut.close()
