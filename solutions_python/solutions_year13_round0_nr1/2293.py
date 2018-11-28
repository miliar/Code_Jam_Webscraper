import time

imput = open("A-large.in", "r").read()




lines = imput.split("\n")


class board():   
    def __init__(self, lines):
        self.rows = (lines[0], lines[1], lines[2], lines[3])
        self.diag1 = lines[0][0] + lines[1][1] + lines[2][2] + lines[3][3]
        self.diag2 = lines[0][3] + lines[1][2] + lines[2][1] + lines[3][0]
        self.cols = (lines[0][0] + lines [1][0] + lines[2][0] + lines[3][0],
                     lines[0][1] + lines [1][1] + lines[2][1] + lines[3][1],
                     lines[0][2] + lines [1][2] + lines[2][2] + lines[3][2],
                     lines[0][3] + lines [1][3] + lines[2][3] + lines[3][3])
        
    def solve(self):
        self.incomplete = False
        for each in self.rows:
            if "." in each:
                self.incomplete = True
            elif each.count("X") + each.count("T") == 4:
                return "X won"
            elif each.count("O") + each.count("T") == 4:
                return "O won"

        for each in self.cols:
            if "." in each:
                self.incomplete = True
            elif each.count("X") + each.count("T") == 4:
                return "X won"
            elif each.count("O") + each.count("T") == 4:
                return "O won"

        for each in [self.diag1, self.diag2]:
            if "." in each:
                self.incomplete = True
            elif each.count("X") + each.count("T") == 4:
                return "X won"
            elif each.count("O") + each.count("T") == 4:
                return "O won"
            
        if not self.incomplete:
            return "Draw"
        else:
            return "Game has not completed"


boardCount = int(lines[0])
boards = {}
for nBoard in range(0, boardCount):
    thisBoard = lines[nBoard*5+1:nBoard*5+5]
    boards[nBoard+1] = board(thisBoard)

f = open("./out.txt", "a")

for game in boards:
    print >> f, "Case #%s:" %game, boards[game].solve()
    
