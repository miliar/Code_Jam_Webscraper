def check(line, player):
    return all(map(lambda i:((i==player) or (i=="T")), line))


class Board:
    def __init__(self, lines):
        self.lines = [l.strip() for l in lines]
    
    def outcome(self):
        
        # check rows
        for i in range(4):
            l = self.lines[i]
            if check(l, "X"):
                return "X won"
            elif check(l, "O"):
                return "O won"
        
        # check cols
        for i in range(4):
            l = "".join([j[i] for j in self.lines])
            if check(l, "X"):
                return "X won"
            elif check(l, "O"):
                return "O won"

        # diags
        for l in ["".join([self.lines[i][i] for i in range(4)]), "".join(self.lines[i][3-i] for i in range(4))]:
            if check(l, "X"):
                return "X won"
            elif check(l, "O"):
                return "O won"

        for l in self.lines:
            if "." in l:
                return "Game has not completed"

        return "Draw"

            

inputFileName = "A-large.in"

fp = open(inputFileName, "r")

lines = fp.readlines()

fpOut = open("outputA.txt", "w")

numCases = int(lines[0].strip())

for c in range(1, numCases+1):
    b = Board(lines[5*c-4:5*c])
    
    fpOut.write("Case #%d: %s\n"%(c, b.outcome()))
    
fp.close()
