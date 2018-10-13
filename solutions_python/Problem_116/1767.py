def getRow( s ):
    return [
        s[0], s[1], s[2], s[3]
    ]

def checkCell( s, scores ):
    if s == 'X':
        return (scores[0],scores[1]+1)
    if s == 'O':
        return (scores[0]+1,scores[1])
    if s == 'T':
        return (scores[0]+1,scores[1]+1)
    return scores
    
def findWinner( board ):
    j = 0
    dots = 0
    #horizontal
    while j < 4:
        i = 0
        (O, X) = (0, 0)
        while i < 4:
            (O, X) = checkCell( board[j][i], (O, X))
            if board[j][i] == '.': dots += 1
            i += 1
        if X == 4: return 'X won'
        if O == 4: return 'O won'
        j += 1

    j=0
    #vertical
    while j < 4:
        i = 0
        (O, X) = (0, 0)
        while i < 4:
            (O, X) = checkCell( board[i][j], (O, X))
            i += 1
        if X == 4: return 'X won'
        if O == 4: return 'O won'
        j += 1

    i=0
    #diagonal
    (O, X) = (0, 0)
    while i < 4:
        (O, X) = checkCell( board[i][i], (O, X))
        i += 1
    if X == 4: return 'X won'
    if O == 4: return 'O won'
    (O, X) = (0, 0)
    i=0
    while i < 4:
        (O, X) = checkCell( board[3-i][i], (O, X))
        i += 1
    if X == 4: return 'X won'
    if O == 4: return 'O won'

    if dots == 0:
        return 'Draw'
    else:
        return 'Game has not completed'
    
input = open('A-large.in','r')
n = int(input.readline())

i = n
ret = ''
while i > 0:
    case = []
    j = 4
    while j > 0:
        case.append(getRow(input.readline()))
        j -= 1
    input.readline()
    i -= 1
    ret += 'Case #'+str(n-i)+': '+findWinner(case)+'\n'
input.close()

output = open('output.txt', 'w')
output.write(ret)
output.close()
