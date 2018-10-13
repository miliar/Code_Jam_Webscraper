import sys

class TicTacToeTomek(object):

    def __init__(self):
        self.fileName = "A-large.in"
        fp = open(self.fileName)
        self.content = fp.read()
        self.testCases = 0
        self.cases = []

    def getFileNAme(self):
        return self.fileName

    def getContent(self):
        return self.content

    def printContent(self):
        print self.content

    def caseHasEmptyCells(self, case):
        for line in case:
            for cell in line:
                if cell == '.' :
                    return False
        
        return True


    def process(self):
        case = []

        for line in open(self.fileName):   
            if line[:-1].isdigit():
                self.testCases = int(line)
                continue

            if line == '\n':
                if len(case) != 0 :
                    self.cases.append(case)
                case = []
            else:
                case.append(list(line[:-1]))


    def whoWins(self, case, Who = 'X'):
        
        # Horizontally
        count = 0
        for line in case:
            count = 0
            for cell in line:
                if cell == Who or cell == 'T': count += 1

            if count == 4 : return True

        # Vertically
        column = 0
        for line in case:
            count = 0
            for lineInner in case:
                if lineInner[column] == Who or lineInner[column] == 'T':
                    count += 1
            if count == 4 : return True
            else: column +=1

        # Diagonal 
        column = 0
        count = 0
        for line in case:
            if line[column] == Who or line[column] == 'T':
                count += 1
            column += 1
        if count == 4: return True 

        # Diagonal inverse
        column = 3
        count = 0
        for line in case:
            if line[column] == Who or line[column] == 'T':
                count += 1
            column -= 1
        if count == 4: return True         


        return False


    def solve(self):
        f = open('output.txt','w')
        i = 0
        for case in self.cases:
            i += 1
            if self.whoWins(case, 'X') == True:
                f.write('Case #' + str(i) + ': X won\n')
            elif self.whoWins(case, 'O') == True:
                f.write('Case #' + str(i) + ': O won\n')
            elif not self.caseHasEmptyCells(case):
                f.write('Case #' + str(i) + ': Game has not completed\n')
            else: f.write('Case #' + str(i) + ': Draw\n')

            if i == self.testCases:
                break

if __name__ == '__main__':
    puzzle = TicTacToeTomek()
    puzzle.process()
    puzzle.solve()
    


