import re

class board:
    def __init__(self,lines ):
        self.b = []
        for line in lines:
            self.b.append([line[0], line[1], line[2],line[3]])
        self.x = False
        self.o = False
        self.complete = 0

    def check_seq(self, seq):
        check = set()
        for elt in seq:
            check.add(elt)
        if {'X', 'O', '.'} & check == {'X'}:
            self.x = True

        elif  ({'X', 'O', '.'} & check == {'O'}):
            self.o = True
        elif  {'.'} & check == set():
            self.complete += 1

    def game_result(self):
        #check rows
        for row in self.b:
            self.check_seq(row)
 
        #check columns
        for i in range(4):
            column = []
            for row in self.b:
                column.append(row[i])
            self.check_seq(column)
   
        #check diags
        diag1 = []
        diag2 = []
        for i in range(4):
            diag1.append(self.b[i][i])
            diag2.append(self.b[3-i][i])
        self.check_seq(diag1)
        self.check_seq(diag2)

        if self.x:
            return 'X won'
        elif self.o:
            return 'O won'
        elif self.complete == 10:
            return 'Draw'
        else:
            return 'Game has not completed'

def print_results(filename, output):
    p = re.compile(r'([.OXT]+)')
    results = []
    f = open(filename, 'r')
    games = int(f.readline()[:-1])
    for i in range(games):
        b = []
        for j in range(4):
            b.append(p.match(f.readline()).group())
        dust = f.readline()
        game = board(b)
        results.append(game.game_result())
    f.close()
    f = open(output, 'w')
    for i,res in enumerate(results):
        f.write('Case #{}: '.format(i+1)+res+'\n')
    f.close()
    
        
                      
