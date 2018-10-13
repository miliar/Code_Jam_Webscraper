import sys, math

class TicTacToeTomek(object):

    def __init__(self):
        self.fileName = "C-small-attempt0.in"
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


    def process(self):
        for line in open(self.fileName):   
            if line[:-1].isdigit():
                self.testCases = int(line)
                continue

            if line != '\n':
                self.cases.append(line[:-1].split(' '))


    def isPalindrome(self, value):
        if str(value) == str(value)[::-1]: return True
        else: return False


    def solve(self):
        f = open('output.txt','w')
        i = 0
        for case in self.cases:
            count = 0
            i += 1
            for x in range(int(case[0]), int(case[1]) + 1):
                squareX = math.sqrt(int(x))
                if int(squareX) == squareX:
                    squareX = int(squareX)
                else: continue

                if self.isPalindrome(x) and self.isPalindrome(squareX):
                    count += 1
            f.write('Case #' + str(i) + ': ' + str(count) + '\n')

            if i == self.testCases:
                break

if __name__ == '__main__':
    puzzle = TicTacToeTomek()
    puzzle.process()
    puzzle.solve()
    


