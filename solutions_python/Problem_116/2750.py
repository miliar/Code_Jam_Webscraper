import operator, sys, random, time

Empty = '.'
__author__ = 'Golfpong'

class BoardGame:
    
    def __init__(self):
        self.pieces = [ [Empty]*4 ]*4
        self.winner = {'X': False, 'O': False}
            
    def split_input(self, n, pieces):
        self.pieces[n] = [ pieces[0], pieces[1], pieces[2], pieces[3] ]

    def check_empty(self):
        for pos_y in range(4):
            for pos_x in range(4):
                if self.pieces[pos_y][pos_x] == Empty:
                    return True
        return False

    def check_winner(self):
        winning_rows = [[(0,0), (0,1) , (0,2), (0,3)],
                        [(1,0), (1,1) , (1,2), (1,3)],
                        [(2,0), (2,1) , (2,2), (2,3)],
                        [(3,0), (3,1) , (3,2), (3,3)],# vertical
                        [(0,0), (1,0) , (2,0), (3,0)],
                        [(0,1), (1,1) , (2,1), (3,1)],
                        [(0,2), (1,2) , (2,2), (3,2)],
                        [(0,3), (1,3) , (2,3), (3,3)],# horizontal
                        [(0,0), (1,1) , (2,2), (3,3)],
                        [(0,3), (1,2) , (2,1), (3,0)],# diagonal
                        ] 
        
        for row in winning_rows:
            pre_check = self.pieces[ row[0][0] ][ row[0][1] ]
            n = 1
            for y,x in row:
                if ( self.pieces[y][x] == pre_check or self.pieces[y][x] == 'T' ) and self.pieces[y][x] != Empty:
                    if self.pieces[y][x] != 'T':
                        pre_check = self.pieces[y][x]
                    
                    n += 1
                else:
                    n = 1
                    break
                
            if n == 5:
                if pre_check == 'X':
                    self.winner['X'] = True
                elif pre_check == 'O':
                    self.winner['O'] = True
            
    def output(self):
        self.check_winner()
        if self.winner['X'] and self.winner['O']:
            return 'Draw'
        elif self.winner['X']:
            return 'X won'
        elif self.winner['O']:
            return 'O won'
        elif self.check_empty():
            return 'Game has not completed'
        else:
            return 'Draw'

def run(input_file, output_file):
    file_input = open(input_file)
    file_output = open(output_file, "w")
    round_game = int(file_input.readline())
    for case in range(round_game):
        board_game = BoardGame()
        
        for count_piece in range(4):
            board_game.split_input(count_piece, str(file_input.readline()[0:4]))
        file_input.readline()

        file_output.write('Case #'+str(case+1)+': '+board_game.output())
        
        if case < round_game - 1:
            file_output.write('\n')

if __name__ == "__main__":
    #run('A-small-attempt0.in','A-small-attempt0.out')
    run(sys.argv[1], sys.argv[2])
