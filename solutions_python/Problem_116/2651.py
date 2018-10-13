'''
Created on Apr 14, 2013

@author: ariel
'''
from common.input_file import GCJInputFile
from common.output_file import GCJOutputFile
import sys

DEBUG = True
FILENAME = r'files\A-large-0.in'

class GameStatus(object):
    X_WON = 'X won'
    O_WON = 'O won'
    DRAW = 'Draw'
    NOT_COMPLETED = 'Game has not completed'

def get_series_status(series):
    x_count = series.count('X')
    o_count = series.count('O')
    t_count = series.count('T')
    dot_count = series.count('.')
    
    if t_count == 1:
        if x_count == 3:
            return GameStatus.X_WON
        elif o_count == 3:
            return GameStatus.O_WON
    elif t_count == 0:
        if x_count == 4:
            return GameStatus.X_WON
        elif o_count == 4:
            return GameStatus.O_WON
    
    return GameStatus.DRAW if dot_count == 0 else GameStatus.NOT_COMPLETED

def get_game_status(game):
    
    rows = game[:]
    cols = [[row[i] for row in game] for i in range(4)]
    diags = [[game[i][i] for i in range(4)], [game[i][3-i] for i in range(4)]]
    
    is_not_completed = False
    
    series = rows + cols + diags
    for s in series:
        result = get_series_status(s)
        if result == GameStatus.NOT_COMPLETED:
            is_not_completed = True
        elif result != GameStatus.DRAW:
            return result
    
    return GameStatus.NOT_COMPLETED if is_not_completed else GameStatus.DRAW
    

def main(filename):
    
    f_in = GCJInputFile(filename)
    output_path = f_in.get_output_filename()
    f_out = GCJOutputFile(output_path)
    
    ncases = f_in.read_integer_num_line()
    
    i = 0
    for i in range(ncases):
        
        curr_game = []
        for j in range(4):
            curr_game.append(f_in.readline().strip())
        
        # skip empty line
        f_in.readline()
        
        game_status = get_game_status(curr_game)

        f_out.write_case_line(i+1, game_status, DEBUG)
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(FILENAME)
    else:
        main(*sys.argv[1:])