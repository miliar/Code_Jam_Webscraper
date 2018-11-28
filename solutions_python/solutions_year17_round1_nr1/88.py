from sys import stdin as cin

data=cin.readline

cases=int(data())

for case in range(1,1+cases):
    line=data().split()
    rows=int(line[0])
    columns=int(line[1])
    board=[list(data().strip()) for i in range(rows)]
    
    seenInitials=False
    #forward pass over rows
    for r in range(len(board)):
        if board[r].count('?')==len(board[r]):
            if seenInitials:
                for c in range(len(board[r])):
                    board[r][c]=board[r-1][c]
            else:
                pass #It will be handled on the reverse pass
        else:
            seenThisRow=False
            #forward pass over the row
            for c in range(len(board[r])):
                if board[r][c]=='?':
                    if seenThisRow:
                        board[r][c]=board[r][c-1]
                else:
                    seenThisRow=True
                    seenInitials=True
            #backward pass over the row
            if seenThisRow:
                for c in range(len(board[r])-1, -1, -1):
                    if board[r][c]=='?':
                        board[r][c]=board[r][c+1]
                    
    #reverse pass over rows
    for r in range(len(board)-1, -1, -1):
        if board[r].count('?')==len(board[r]):
            board[r]=board[r+1]
        
    
    print('Case #'+str(case)+':')
    for row in board:
        for char in row:
            print(char, end='')
        print()