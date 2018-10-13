#! /usr/bin/python

import sys

def read_file():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        num_games = int(f.readline())
        game = {(x,y):0 for x in range(4) for y in range(4)}
        
        for game_num in range(num_games):
            period_count = 0
            for row in range(4):
                col = 0
                line = f.readline()
                for mark in line:
                    if mark == '\n':
                        break
                    elif mark == 'O':
                        mark_value = 1
                    elif mark == 'X':
                        mark_value = 2
                    elif mark == 'T':
                        mark_value = 100
                    else:
                        mark_value = 0
                        period_count = 1
                        
                    game[(col, row)] = mark_value
                    col += 1
            game_state = analyze_game(game, period_count)
            print 'Case #%i: %s' % (game_num + 1, game_state)
            f.readline() # Throw away newline

def analyze_game(game, period_count):
    forward_diag = [(x,x) for x in range(4)]
    backward_diag = [(3,0), (2,1), (1,2), (0,3)]

    forward_val = 1
    backward_val = 1

    for point in forward_diag:
        forward_val *= game[point]
    if forward_val == 1 or forward_val == 100:
        return 'O won' 
    elif forward_val == 16 or forward_val == 800:
        return 'X won'

    for point in backward_diag:
        backward_val *= game[point]
    if backward_val == 1 or backward_val == 100:
        return 'O won' 
    elif backward_val == 16 or backward_val == 800:
        return 'X won'
       
    for x in range(4):
        row_val = 1
        for y in range(4):
            row_val *= game[(x,y)]

        if row_val == 1 or row_val == 100:
            return 'O won' 
        elif row_val == 16 or row_val == 800:
            return 'X won'

    for y in range(4):
        col_val = 1
        for x in range(4):
            col_val *= game[(x,y)]

        if col_val == 1 or col_val == 100:
            return 'O won' 
        elif col_val == 16 or col_val == 800:
            return 'X won'
    
    
    if period_count > 0:
        return 'Game has not completed'
    else:
        return 'Draw'

def main():
    read_file()

if __name__ == '__main__':
    main()
