fileToUse = open("A-large.in", "r")
testCount = int(fileToUse.readline())

output = []

def DoTrial(sequence, blueList, orangeList):
    bluePosition = 1
    orangePosition = 1
    time = 0
    buttonPressed = False

    while True:
        time += 1
        buttonPressed = False
        if len(orangeList) > 0:
            if orangeList[0] > orangePosition:
                orangePosition += 1
            elif orangeList[0] == orangePosition:
                if sequence[0][0] == "O":
                    buttonPressed = True
                    del orangeList[0]
                    del sequence [0]
            else:
                orangePosition -= 1
        if len(blueList) > 0:
            if blueList[0] > bluePosition:
                bluePosition += 1
            elif blueList[0] == bluePosition:
                if sequence[0][0] == "B" and buttonPressed == False:
                    del blueList[0]
                    del sequence [0]
            else:
                bluePosition -= 1

        if len(sequence) == 0:
            return time


for i in range(0, testCount):
    line = fileToUse.readline()
    data = line.split(" ")
    buttonCount = int(data[0])
    sequence = []
    blueList = []
    orangeList = []
    for j in range(0, buttonCount):
        sequence.append((data[1 + j*2], int(data[2 + j*2])))
        if sequence[j][0] == "O":
            orangeList.append(int(data[2 + j*2]))
        else:
            blueList.append(int(data[2 + j*2]))
    output.append(DoTrial(sequence, blueList, orangeList))

outFile = open("Output1.out", "w")

for i in range(0, len(output)):
    outFile.write("Case #" + str(i + 1) + ": " + str(output[i]) + "\n")

outFile.close()





