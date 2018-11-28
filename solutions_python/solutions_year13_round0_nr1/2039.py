def readcase(line1, line2, line3, line4):
    game = [[line1[0],line1[1],line1[2],line1[3]] , [line2[0],line2[1],line2[2],line2[3]] , [line3[0],line3[1],line3[2],line3[3]] , [line4[0],line4[1],line4[2],line4[3]]]
    return game

def solvecase(origgame, number):
    rotatedgame=zip(*origgame[::-1])
    finishedgame=True
    for game in [origgame, rotatedgame]:
        for i in range(4):
            # Scan for lines
            line = "".join(game[i])
            if '.' not in line:
                if line.count('T')<2:
                    if line.count('X')+line.count('T')==4:
                        return ("Case #"+str(number)+": X won")
                    if line.count('O')+line.count('T')==4:
                        return ("Case #"+str(number)+": O won")
            else:
                finishedgame=False
        line = game[0][0]+game[1][1]+game[2][2]+game[3][3]
        if line.count('X')+line.count('T')==4:
           return ("Case #"+str(number)+": X won") 
        if line.count('O')+line.count('T')==4:
           return ("Case #"+str(number)+": O won")         
        
    if finishedgame==True:
        return ("Case #"+str(number)+": Draw")
    else:
        return ("Case #"+str(number)+": Game has not completed")

lines = open("file1.txt").readlines()
del lines[0]
for i in range((len(lines)/5)+1):
    case = readcase(lines[i*5+0], lines[i*5+1], lines[i*5+2], lines[i*5+3])
    print solvecase(case, i+1)