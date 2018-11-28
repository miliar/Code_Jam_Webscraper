def determine_outcome(board):
    winning_config = [ (0,1,2,3), (4,5,6,7), (8,9,10,11), (12,13,14,15), \
                       (0,4,8,12), (1,5,9,13), (2,6,10,14), (3,7,11,15), \
                       (0,5,10,15), (3,6,9,12)]
    for config in winning_config:
        possible_winner = 'T'
        for i in config:
            if possible_winner == 'T':
                possible_winner = board[i]
            elif possible_winner != board[i] and possible_winner != 'T' and board[i] != 'T'  :
                possible_winner = 'Q'
                break
        if possible_winner == 'X' or possible_winner == 'O':
            return possible_winner + ' won'
    if '.' in board:
        return 'Game has not completed'
    return 'Draw'

if __name__ == '__main__':
    number = int(input())
    for i in range(number):
        board = input() + input() + input() + input()+ input()
        print("Case #" + str(i+1) + ": " + determine_outcome(board))
