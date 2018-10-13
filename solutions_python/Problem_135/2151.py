def getBoard():
    board = []
    for i in range(4):
        row = input()
        row = row.split()
        for i in range(4):
            row[i] = int(row[i])
        board.append(row)
    return board

def findCommon(a, b):
    count = 0
    thing = 0
    for i in a:
        if i in b:
            count += 1
            thing = i
    return count, thing

numTests = int(input())
for i in range(numTests):
    rowA = int(input())
    boardA = getBoard()[rowA - 1]
    rowB = int(input())
    boardB = getBoard()[rowB - 1]
    temp = findCommon(boardA, boardB)
    print("Case #" + str(i + 1) + ": ", end="")
    if temp[0] == 0:
        print("Volunteer cheated!")
    elif temp[0] > 1:
        print("Bad magician!")
    elif temp[0] == 1:
        print(temp[1])
