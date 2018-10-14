from copy import deepcopy

class TicTacTomek:
    def __init__(self, m):
        self.rows = m
        self.cols = zip(*m)
        dimen = len(m[0])
        self.diags = zip(*[(m[x][x], m[x][dimen-x-1]) for x in range(dimen)])
        self.containsEmpty = False
        
    def checkGroup(self, rows, c):
        for row in rows:
            found = True
            for item in row:
                if item == '.':
                    self.containsEmpty = True
                if item not in c:
                    found = False
                    break
            if found:
                return True
        return False
        
    def check(self):
        if self.checkGroup(self.rows, 'XT') or self.checkGroup(self.cols, 'XT') or self.checkGroup(self.diags, 'XT'):
            return 'X won'
        elif self.checkGroup(self.rows, 'OT') or self.checkGroup(self.cols, 'OT') or  self.checkGroup(self.diags, 'OT'):
            return 'O won'
        elif self.containsEmpty:
            return 'Game has not completed'
        return 'Draw'
        
        

def main():
    for caseNumber in xrange(int(raw_input(""))):
        m = [list(raw_input("")) for _ in range(4)]
        try: raw_input("");
        except: pass
        
        print "Case #%d:"%(caseNumber+1), TicTacTomek(m).check()
        
if __name__ == '__main__':
    main()
