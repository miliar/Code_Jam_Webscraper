def win(board,k,color):
    canHor = True
    canVert = True
    canDiagF = True
    canDiagB = True
    for r in range(0,len(board)):
        for c in range(0,len(board[r])):
            for i in range(0,k) :
                if canHor:
                    canHor = test(board,r,c+i,color)
                if canVert:
                    canVert = test(board,r+i,c,color)
                if canDiagF:
                    canDiagF = test(board,r+i,c+i,color)
                if canDiagB:
                    canDiagB = test(board,r+i,c-i,color)
                
            if canHor or canVert or canDiagF or canDiagB:
                return True
            else:
                canHor = True
                canVert = True
                canDiagF = True
                canDiagB = True
    return False
   
def test(board,r,c,color):
    if  r<len(board) and r>=0:
        if c<len(board[r]) and c>=0:
            return board[r][c]==color
    return False

with open('A-large .in') as input, open('out.txt', 'w') as output:
    header = input.readline().split(" ")
    cases = int(header[0]);
    for i in range(1,cases+1):
        caseHdr = input.readline().strip().split(" ")
        size = int(caseHdr[0])
        k = int(caseHdr[1])
        board = []
        for j in range(0,size):
            line = input.readline().strip()
            chars = list(line)
            row = []
            for c in reversed(range(0,len(line))):
                if(chars[c]!='.'):
                    row.append(chars[c])
            board.append(row)
        winRed = win(board,k,'R')
        winBlue = win(board,k,'B')
        outcome = "Neither"
        if(winRed and winBlue):
            outcome = "Both"
        elif (winRed):
            outcome = "Red"
        elif (winBlue):
            outcome = "Blue"    
        print('Case #{}: {}\n'.format(i,outcome))
        output.write('Case #{}: {}\n'.format(i,outcome))
    output.close()
    print("Done")