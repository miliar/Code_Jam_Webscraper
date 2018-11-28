
    # try:
    #     # open the hte file for reading
    #     hteFile = open('downloads/' + fileName, 'rb')

    #     hteRecords = list(csv.reader(hteFile))

    #     hteHeaders = hteRecords[0]

    #     # close the file
    #     hteFile.close()

inputFile = open('A-small-attempt0.in', 'rb')

outputFile = open('A-small-attempt0.out', 'w')

T = int(inputFile.readline().rstrip("\n"))

for i in range(0, T):

    c1 = int(inputFile.readline().rstrip("\n"))

    for j in range(1, c1):
        #skip the lines
        inputFile.readline()

    row1 = inputFile.readline().rstrip("\n").split(" ")

    for j in range(c1, 4):
        #skip the remaining lines
        inputFile.readline()

    c2 = int(inputFile.readline().rstrip("\n"))

    for j in range(1, c2):
        #skip the lines
        inputFile.readline()

    row2 = inputFile.readline().rstrip("\n").split(" ")

    for j in range(c2, 4):
        #skip the remaining lines
        inputFile.readline()

    intersection = set(row1) & set(row2)

    if len(intersection) == 0:
        answer = "Volunteer cheated!"
    elif len(intersection) == 1:
        answer = intersection.pop()
    else:
        answer = "Bad magician!"
    outputFile.write("Case #%d: %s\n" % (i+1, answer))

inputFile.close()
outputFile.close()