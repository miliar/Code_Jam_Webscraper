inputFile = open("A-small-attempt0.in", 'r')

count =  int(inputFile.readline())

arrangementOne = [[], [], [], []]
arrangementTwo = [[], [], [], []]

firstRowNumber = 0
secondRowNumber = 0

for y in range(1, count+1):
    firstRowNumber = int(inputFile.readline()) - 1
    for x in range(0, 4):
        arrangementOne[x] = [int(i) for i in inputFile.readline().split()]
    secondRowNumber = int(inputFile.readline()) - 1
    for x in range(0, 4):
        arrangementTwo[x] = [int(i) for i in inputFile.readline().split()]
    intersectCards = set(arrangementOne[firstRowNumber]).intersection(arrangementTwo[secondRowNumber])
    if len(intersectCards) == 1:
        print "Case #%s:" % y, list(intersectCards)[0]
    elif len(intersectCards) > 1:
        print "Case #%s: Bad magician!" % y
    else:
        print "Case #%s: Volunteer cheated!" % y