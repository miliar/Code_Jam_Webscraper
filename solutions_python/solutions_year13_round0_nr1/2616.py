winningCombos = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15],\
                 [0,4,8,12],[1,5,9,13],[2,6,10,14], [3,7,11,15],\
                 [0,5,10,15], [12,9,6,3]]

gameFile = open('A-large.in')
outputFile = open('output.txt', 'w')
numCases = int(gameFile.readline().strip())
for i in range(numCases):
    hasWinner = False
    points = []
    for j in range(4):
        line = gameFile.readline().strip()
        points.extend([letter for letter in line])
        
    for combo in winningCombos:
        if all([points[k]=='X' or points[k]=='T' for k in combo]):
            outputFile.write("Case #{0}: X won\n".format(i + 1))
            hasWinner = True
            break
        elif all([points[k]=='O' or points[k]=='T' for k in combo]):
            outputFile.write("Case #{0}: O won\n".format(i + 1))
            hasWinner = True
            break
    if not hasWinner and '.' in points:
        outputFile.write("Case #{0}: Game has not completed\n".format(i + 1))
    elif not hasWinner:
        outputFile.write("Case #{0}: Draw\n".format(i + 1))
    gameFile.readline()
    
outputFile.close()
gameFile.close()