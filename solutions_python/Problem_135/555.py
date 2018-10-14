from collections import deque

input = open('./A-small-attempt0.in', 'r').readlines()
output = open('./A-small-attempt0.out', 'w') 

inputQueue = deque(input)
testCases = int(inputQueue.popleft())
for i in range(0, testCases):
    outputString = "Case #"+str(i+1)+": "
    sets = list()
    for j in range(0, 2):
        named = int(inputQueue.popleft())-1
        board = list()
        for k in range(0,4):
            board.append(inputQueue.popleft().split())
        sets.append(set(board[named]))
        print("j", sets[j])
    commonCards = sets[0] & sets[1]
    print("common", commonCards)

    if len(commonCards) > 1:
        outputString+= "Bad magician!"
    if len(commonCards) == 0:
        outputString+= "Volunteer cheated!"
    if len(commonCards) == 1:
        outputString+= commonCards.pop()
    print(outputString)
    outputString += "\n"
    output.write(outputString)
output.close()