import sys

class board:
    def __init__(self, file):
        self.pieces = []
        for i in range(4):
            line = file.readline()
            tmp = [line[0], line[1], line[2], line[3]]
            self.pieces.append(tmp)
        file.readline()
    def testWin(self, line):
        state = line[0]
        for i in range(1,4):
            if state == "T":
                state = line[i]
            elif line[i] == "T":
                pass
            elif line[i] == ".":
                state = "."
                break
            elif line[i] != state:
                state = " "
                break
        return state
    def getResult(self):
        boardFilled = True
        for y in range(4):
            result = self.testWin(self.pieces[y])
            if result == "X":
                return "X won"
            elif result == "O":
                return "O won"
            elif result == ".":
                boardFilled = False
        for x in range(4):
            result = self.testWin([self.pieces[n][x] for n in range(4)])
            if result == "X":
                return "X won"
            elif result == "O":
                return "O won"
        result = self.testWin([self.pieces[n][n] for n in range(4)])
        if result == "X":
            return "X won"
        elif result == "O":
            return "O won"
        result = self.testWin([self.pieces[3-n][n] for n in range(4)])
        if result == "X":
            return "X won"
        elif result == "O":
            return "O won"
        elif boardFilled:
            return "Draw"
        return "Game has not completed"
        
def main():
    f = sys.stdin
    
    num = int(f.readline())
    for i in range(num):
        current = board(f)
        print("Case #"+str(i+1)+": ", end='')
        print(current.getResult())

    #f.close()

if __name__ == '__main__':
    main()
