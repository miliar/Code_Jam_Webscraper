FILE_IN = "A-large.in"
FILE_OUT = "A-large.out"
NEWLINE = '\n'

class Board(object):
    def __init__(self, board):
        self.rows = []
        for i in range(4):
            self.rows.append(board[i])
        
        self.columns = [[],[],[],[]]
        for i in range(4):
            self.columns[0].append(self.rows[i][0])
            self.columns[1].append(self.rows[i][1])
            self.columns[2].append(self.rows[i][2])
            self.columns[3].append(self.rows[i][3])
            
        self.diagonal1 = []
        self.diagonal2 = []
        
        for i in range(4):
            self.diagonal1.append(self.rows[i][i])
            self.diagonal2.append(self.rows[i][3-i])
            
    def get_state(self):
        if self._is_win("X"):
            return "X won"
        if self._is_win("O"):
            return "O won"
        if self._is_game_completed():
            return "Game has not completed"
        else:
            return "Draw"
        
    def _is_win(self,player):
        result = False
        
        for row in self.rows:
            result = result or self._check(row,player) 
        
        for col in self.columns:
            result = result or self._check(col, player)
            
        result = result or self._check(self.diagonal1, player) or self._check(self.diagonal2, player)
        
        return result            
    
    def _check(self, l, p):
        return l.count(p) == 4 or (l.count(p) == 3 and l.count("T") == 1)      
    
    def _is_game_completed(self):
        return "." in self.rows[0] or "." in self.rows[1] or "." in self.rows[2] or "." in self.rows[3] 
        


if __name__ == '__main__':
    f = open(FILE_IN, "r")
    f_out = open(FILE_OUT, "w")
    lines = f.readlines()
    num_of_cases = int(lines[0])
    j = 1
    lines_out = []
    for i in range(num_of_cases):
        l = [lines[j], lines[j+1], lines[j+2], lines[j+3]]
        b = Board(l)
        result = "Case #%d: " % (i+1) + b.get_state() + NEWLINE
        lines_out.append(result)
        j += 5
    
    f_out.writelines(lines_out)
    f.close()
    f_out.close()
    print 'done.'
