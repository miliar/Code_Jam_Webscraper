class Board:
    
    def __init__(self, matrix):
        self.board = matrix
    
    def whoWon(self):
        winner = ""
        for i in self.board:
            for j in i:
                winner = winner + j
            if winner == "XXXX" or winner == "XXXT" or winner == "XXTX" or winner == "XTXX" or winner == "TXXX":
                return "X won"
            elif winner == "OOOO" or winner == "OOOT" or winner == "OOTO" or winner == "OTOO" or winner == "TOOO":
                return "O won"
            winner = ""
        
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                winner = winner + self.board[j][i]
                if winner == "XXXX" or winner == "XXXT" or winner == "XXTX" or winner == "XTXX" or winner == "TXXX":
                    return "X won"
                elif winner == "OOOO" or winner == "OOOT" or winner == "OOTO" or winner == "OTOO" or winner == "TOOO":
                    return "O won"
            winner = ""
        
        for i in range(len(self.board)):
            winner = winner + self.board[i][i]
            if winner == "XXXX" or winner == "XXXT" or winner == "XXTX" or winner == "XTXX" or winner == "TXXX":
                return "X won"
            elif winner == "OOOO" or winner == "OOOT" or winner == "OOTO" or winner == "OTOO" or winner == "TOOO":
                return "O won"
        winner = ""
        
        for i in range(len(self.board)):
            winner = winner + self.board[i][(len(self.board)-1)-i]
            if winner == "XXXX" or winner == "XXXT" or winner == "XXTX" or winner == "XTXX" or winner == "TXXX":
                return "X won"
            elif winner == "OOOO" or winner == "OOOT" or winner == "OOTO" or winner == "OTOO" or winner == "TOOO":
                return "O won"
        winner = ""
        
    def isDraw(self):
        for i in self.board:
            if "." in i:
                return "Game has not completed"
        return "Draw"
    
    def gameStatus(self):
        status = self.whoWon()
        if not status:
            status = self.isDraw()
        return status

if __name__ == '__main__':
    fi = open("A-small-attempt0.in")
    text = fi.read()
    token = text.split()
    cases = int(token[0])
    del token[0]
    for i in range(cases):
        matrix = [list(token[i*4]), list(token[i*4+1]), list(token[i*4+2]), list(token[i*4+3])]
        game = Board(matrix)
        print "Case #" + str(i+1) + ": " + game.gameStatus()
    pass