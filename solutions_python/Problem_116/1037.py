

if __name__ == "__main__":
    numberOfTests = (int)(input())
    
    board = []
    for x in range(numberOfTests):
        board = []
        for a in range(4):
            board.append(input())
        input()
    
        someone_won = '0';
        #test line
        for line in range(4):
            lineType = '-1'
            for pos in range(len(board[line])):
                eachChar = board[line][pos]
                if lineType == 'O':
                    if eachChar == 'X' or eachChar == '.':
                        break
                if lineType == 'X':
                    if eachChar == 'O' or eachChar == '.':
                        break
                if lineType == '-1':
                    if eachChar == '.':
                        break
                    if eachChar == 'O' or eachChar == 'X':
                        lineType = eachChar
                if pos == 3:
                    someone_won = lineType + ' won'
        
        #test column
        if someone_won == '0':
            for line in range(4):
                lineType = '-1'
                for pos in range(len(board[line])):
                    eachChar = board[pos][line]
                    if lineType == 'O':
                        if eachChar == 'X' or eachChar == '.':
                            break
                    if lineType == 'X':
                        if eachChar == 'O' or eachChar == '.':
                            break
                    if lineType == '-1':
                        if eachChar == '.':
                            break
                        if eachChar == 'O' or eachChar == 'X':
                            lineType = eachChar
                    if pos == 3:
                        someone_won = lineType + ' won'
            
        #test diagonal
        if someone_won == '0':
            for line in range(1):
                lineType = '-1'
                for pos in range(len(board[line])):
                    eachChar = board[pos][pos]
                    if lineType == 'O':
                        if eachChar == 'X' or eachChar == '.':
                            break
                    if lineType == 'X':
                        if eachChar == 'O' or eachChar == '.':
                            break
                    if lineType == '-1':
                        if eachChar == '.':
                            break
                        if eachChar == 'O' or eachChar == 'X':
                            lineType = eachChar
                    if pos == 3:
                        someone_won = lineType + ' won'
        
        #test diagonal
        if someone_won == '0':
            for line in range(1):
                lineType = '-1'
                for pos in range(len(board[line])):
                    eachChar = board[pos][3-pos]
                    if lineType == 'O':
                        if eachChar == 'X' or eachChar == '.':
                            break
                    if lineType == 'X':
                        if eachChar == 'O' or eachChar == '.':
                            break
                    if lineType == '-1':
                        if eachChar == '.':
                            break
                        if eachChar == 'O' or eachChar == 'X':
                            lineType = eachChar
                    if pos == 3:
                        someone_won = lineType + ' won'
        if someone_won == '0':
            for pos in range(len(board)):
                if '.' in board[pos]:
                    someone_won = 'Game has not completed'
                    break
                if pos == 3:
                    someone_won = 'Draw'
        print('Case #'+str(x+1)+': ' + someone_won)
            