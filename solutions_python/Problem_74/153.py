INPUT_FILE = r'C:\Downloads\FromFirefox\A-large.in'
OUTPUT_FILE = r'C:\Users\Assaf\Fun\codeJam\A-large.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def findNextMove(tasks, index, color):
    if None == index:
        return None
    index += 1
    while True:
        if index >= len(tasks):
            return None
        if tasks[index][0] == color:
            return index
        index += 1
    return index

def solveQuestion(tasks):
    OBot = 1
    BBot = 1
    OIndex = findNextMove(tasks, -1, 0)
    BIndex = findNextMove(tasks, -1, 1)
    counter = 0
    while not (None == OIndex and None == BIndex):
        if None == BIndex:
            turn = 0
        elif None == OIndex:
            turn = 1
        elif OIndex < BIndex:
            turn = 0
        else:
            turn = 1
        if None != OIndex:
            OTask = tasks[OIndex]
            if OBot < OTask[1]:
                OBot += 1
            elif OBot > OTask[1]:
                OBot -= 1
            elif 0 == turn:
                OIndex = findNextMove(tasks, OIndex, 0)
        if None != BIndex:
            BTask = tasks[BIndex]
            if BBot < BTask[1]:
                BBot += 1
            elif BBot > BTask[1]:
                BBot -= 1
            elif 1 == turn:
                BIndex = findNextMove(tasks, BIndex, 1)
        counter += 1
        #print counter, OIndex, BIndex, turn, OBot, BBot
    return str(counter)

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    # Don't forget to read length of a list
    line = inputFile.readline().split(' ')
    l = int(line[0])
    task = []
    for i in xrange(l):
        task.append(([0,1][line[i*2+1]=='B'], int(line[i*2+2])))
    result = solveQuestion(task)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
