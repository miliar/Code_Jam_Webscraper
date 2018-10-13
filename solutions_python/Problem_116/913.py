
def Win(player, board):
    for i in range(4):
        flag = True
        for j in range(4):
            if board[i][j] is player or board[i][j] is 'T':
                pass
            else:
                flag = False
                break

        if flag is True:
            break

    if flag is False:
        for i in range(4):
            flag = True
            for j in range(4):
                if a[j][i] is player or a[j][i] is 'T':
                    pass
                else:
                    flag = False
                    break

            if flag is True:
                break
                
    if flag is False:
        flag = True
        for i in range(4):
            if a[i][i] is player or a[i][i] is 'T':
                pass
            else:
                flag = False
                break

    if flag is False:
        flag = True
        for i in range(4):
            if a[i][3 - i] is player or a[i][3 - i] is 'T':
                pass
            else:
                flag = False
                break

    return flag

fileName = input()
f = open(fileName , 'r')


outFile = "result.out"
out = open(outFile , 'w')

numTest = f.readline().strip()

print(numTest)

for i in range(int(numTest)):
    a = []
    for j in range(4):
        a.append(f.readline().strip())
        
    result = "Case #" + str(i + 1) + ": "

    if Win('X', a):
        result = result + "X won"
    elif Win('O', a):
        result = result + "O won"

    else:
        dotFlag = False
        
        for j in range(4):
            for k in range(4):
                if a[j][k] is '.':
                    dotFlag = True
                    break
                
        if dotFlag is True:
            result = result + "Game has not completed"
        else:
            result = result + "Draw"
            
    print(result)
    out.write(result)
    if i is not int(numTest) - 1:
        out.write('\n')
    f.readline().strip()
    
f.close()
out.close()
