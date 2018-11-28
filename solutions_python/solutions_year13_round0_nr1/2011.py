#!/usr/bin/python

def is_draw(board):
    return not '.' in board

def check_line(line):
    if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
        return "X"
    if line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
        return "O"
    return "None"

def game_state(board):
    lines = [board[0:4], board[4:8], board[8:12], board[12:16],
             board[0:16:4], board[1:16:4], board[2:16:4],
             board[3:16:4], board[0:16:5], board[3:13:3]]
    for line in lines:
        result = check_line(line)
        if result != "None":
            return "%s won" % (result)
    if is_draw(board):
        return "Draw"
    else:
        return "Game has not completed"

def main():
    T = input()
    for t in range(T):
        board = ""
        board += raw_input() + raw_input() + raw_input() + raw_input()
        raw_input()
        print "Case #%d: %s" % (t + 1, game_state(board))

if __name__ == "__main__":
    main()
