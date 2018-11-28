input_file = open('C:\Programs\programing\python26\contest2013\A-large.in', 'r')
output_file = open('C:\Programs\programing\python26\contest2013\A-large.out', 'w')

number_players = 0
current_player = 1

def check_win(player, board):
    adj_board = board.replace('T', player)
    counter = 0
    for i in range(0,16,5):
        counter += adj_board[i].count(player)
    if counter == 4:
        return True
    
    counter = 0
    for i in range(0,10,3):
        counter += adj_board[i+3].count(player)
    if counter == 4:
        return True
    
    for i in range(0,4):
        counter = 0
        for j in range(0,13,4):
            counter += adj_board[j + i].count(player)
        if counter == 4:
            return True
     
    for i in range(0,4):
        counter = 0
        for j in range(0,4):
            counter += adj_board[i*4 + j].count(player)
        if counter == 4:
            return True

    return False

board = ''
for line in input_file:
    if number_players==0:
        number_players = int(line)
    elif line == '\n':
        pass
    else:
        board = board + line[0:4]
        if len(board) == 16:
            if (check_win('X', board)):
                result = 'X won'
            elif(check_win('O', board)):
                result = 'O won'
            elif((board.count('X') + board.count('T') + board.count('O')) == 16):
                result = 'Draw'
            else:
                result = 'Game has not completed'
            output_file.write('Case #' + str(current_player) + ': ' + result)
            if current_player != number_players:
                output_file.write('\n')
            current_player += 1
            board = ''
input_file.close()
output_file.close()

    
        
        
        
    
