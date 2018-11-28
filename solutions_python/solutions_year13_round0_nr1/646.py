'''
Created on 13.04.2013

@author: Great Combinator
'''

class TicTacToeAnalyzer(object):
    def __init__(self, inp, outp):
        self.input_path = inp
        self.output_path = outp
        self.numberOfTCs = 0
        self.boards = {}
        self.values = {'.': 1,
                       'X': 10,
                       'O': 100,
                       'T': 1000}
        self.read_boards()
        
    def read_boards(self):
        input_file = open(self.input_path, 'r')
        lines = input_file.readlines()
        self.numberOfTCs = int(lines[0].strip())
        idx = 0
        while idx < self.numberOfTCs:
            self.boards['board_%s' % (idx+1)] = {}
            self.boards['board_%s' % (idx+1)][0] = [self.values[elem.strip()] for elem in list(lines[5*idx+1].strip())]
            self.boards['board_%s' % (idx+1)][1] = [self.values[elem.strip()] for elem in list(lines[5*idx+2].strip())]
            self.boards['board_%s' % (idx+1)][2] = [self.values[elem.strip()] for elem in list(lines[5*idx+3].strip())]
            self.boards['board_%s' % (idx+1)][3] = [self.values[elem.strip()] for elem in list(lines[5*idx+4].strip())]
            
            #0-3 row represenations; 4-7 column representations; 8, 9 diagonal representations
            status_representation = self.boards['board_%s' % (idx+1)]['status_representation'] = {}
            counter = 0;
            while counter < 10:
                status_representation[counter] = 0
                counter += 1
                
            row = 0
            column = 0
            while row < 4:
                column = 0
                while column < 4:
                    status_representation[row] += self.boards['board_%s' % (idx+1)][row][column]
                    status_representation[4+column] += self.boards['board_%s' % (idx+1)][row][column]
                    if row == column:
                        status_representation[8] += self.boards['board_%s' % (idx+1)][row][column]
                    elif row + column == 3:
                        status_representation[9] += self.boards['board_%s' % (idx+1)][row][column]
                    
                    column += 1
                row += 1
            idx += 1
    
    def analyze(self, board_idx):
        x_win = 'X won'
        o_win = 'O won'
        draw = 'Draw'
        not_finished = 'Game has not completed'
        
        result = draw
        
        condition_idx = 0
        while condition_idx < 10:
            #print board_idx, self.boards['board_%s' % (board_idx)]['status_representation'][condition_idx]
            if self.boards['board_%s' % (board_idx)]['status_representation'][condition_idx] % 1000 % 100 % 10 != 0:
                result = not_finished
                condition_idx += 1
                continue
            elif self.boards['board_%s' % (board_idx)]['status_representation'][condition_idx] in [40, 1030]:
                result = x_win
                condition_idx += 1
                break
            elif self.boards['board_%s' % (board_idx)]['status_representation'][condition_idx] in [400, 1300]:
                result = o_win
                condition_idx += 1
                break
            condition_idx += 1
        return result
        
    def solve(self):
        output_file = open(self.output_path, 'w')
        idx = 1
        while idx <= self.numberOfTCs:
            output_file.write('Case #%s: %s\n' % (idx, self.analyze(idx)))
            idx += 1
            
            
def main():
    input_path = r'C:\Users\Great Combinator\workspace\GCJ2013\tic_tac_toe\A-large.in'
    output_path = r'C:\Users\Great Combinator\workspace\GCJ2013\tic_tac_toe\A-large.out'
    problem = TicTacToeAnalyzer(input_path, output_path)
    problem.solve()
    
if __name__ == '__main__':
    main()