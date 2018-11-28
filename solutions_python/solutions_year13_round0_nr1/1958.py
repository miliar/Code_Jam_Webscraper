import sys

class Board(object):

    def __init__(self, case, rows):
        self.case = case
        self.rows = rows
    
    def get_score(self):
        x_has_won = self.has_score('X')
        o_has_won = self.has_score('O')
        
        if x_has_won and o_has_won:
            return 'Draw'
        if x_has_won:
            return 'X won'
        if o_has_won:
            return 'O won'
        for i in range(4):
            if '.' in self.rows[i]:
                return 'Game has not completed'
        return 'Draw'
            
    def has_score(self, player):
        for i in range(4):
            if self.is_horizontal(i, player):
                return True
            if self.is_vertical(i, player):
                return True
        if self.is_schuin1(player):
                return True
        if self.is_schuin2(player):
                return True
        if self.is_schuin3(player):
                return True
        if self.is_schuin4(player):
                return True
        
    def is_schuin1(self, player):  
        for i in range(4):
            if not self.rows[i][i] == player and not self.rows[i][i] == 'T':
                return False
        return True
        
    def is_schuin2(self, player):  
        for i in range(4):
            if not self.rows[3-i][i] == player and not self.rows[3-i][i] == 'T':
                return False
        return True
        
    def is_schuin3(self, player):  
        for i in range(4):
            if not self.rows[i][3-i] == player and not self.rows[i][3-i] == 'T':
                return False
        return True
        
    def is_schuin4(self, player):  
        for i in range(4):
            if not self.rows[3-i][3-i] == player and not self.rows[3-i][3-i] == 'T':
                return False
        return True
            
    def is_horizontal(self, i, player):
        for j in range(4):
            if not self.rows[i][j] == player and not self.rows[i][j] == 'T':
                return False
        return True
        
    def is_vertical(self, j, player):
        for i in range(4):
            if not self.rows[i][j] == player and not self.rows[i][j] == 'T':
                return False
        return True
        
def read_input(stream): 
    line1 = stream.readline()
    number_of_cases = int(line1.strip())
    for i in range(number_of_cases):
        rows = []
        rows.append(stream.readline().strip())
        rows.append(stream.readline().strip())
        rows.append(stream.readline().strip())
        rows.append(stream.readline().strip())
        yield Board(i+1, rows)
        stream.readline().strip()
    
        
if __name__ == '__main__':
    for x in read_input(sys.stdin):
        print 'Case #{0}: {1}'.format(x.case, x.get_score())
        