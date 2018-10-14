f=open('asd.in','r')
f2=open('output','w')
totalTestCases = int(f.readline().strip())

winner =''

def check(lis):
    global winner
    winner=''
    if lis.count('T')>0:
        if lis.count('X')==3:        
            winner = 'X'
        if lis.count('O')==3:        
            winner = 'O'
    else:
        if lis.count('X')==4:        
            winner = 'X'
        if lis.count('O')==4:        
            winner = 'O'
    if winner:
        raise Exception
        
def win(matrix):
    global winner
    #horizontal check
    try:
        for p in range(0,4):
            check(matrix[p])
            check("".join([matrix[0][p],matrix[1][p],matrix[2][p],matrix[3][p]]))
        check([matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3]])
        check([matrix[0][3],matrix[1][2],matrix[2][1],matrix[3][0]])
    except Exception:
        return winner

for i in range(0,totalTestCases):
    print "Case #%d: " % (i+1),
    f2.write("Case #%d: " % (i+1))
    matrix = []
    for j in range(0,5):
        matrix.append(f.readline().strip())
    r = win(matrix)
    if r=='X':
        print "X won"
        f2.write("X won\n")
    elif r=='O':
        print "O won"
        f2.write("O won\n")
    else:
        drawFlag = 1
        for k in range(0,4):
            if '.' in matrix[k]:
                print "Game has not completed"
                f2.write("Game has not completed\n")
                drawFlag = 0
                break
        if drawFlag:
            f2.write("Draw\n")
            print "Draw"
f2.close()
        
