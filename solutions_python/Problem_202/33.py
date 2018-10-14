from sys import stdin, stdout
import sys

sys.setrecursionlimit(1000000)

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.N, count = (int(_) for _ in stdin.readline().split())
        self.originPlacement = []
        for i in range(count) :
            mode, r, c = stdin.readline().split()
            self.originPlacement.append((mode, int(r) - 1, int(c) - 1))

    def calculate(self) :

        self.originGridX = [[0 for i in range(self.N)] for j in range(self.N)]
        self.originGridPlus = [[0 for i in range(self.N)] for j in range(self.N)]
        for mode, row, col in self.originPlacement :
            if mode == '+' :
                self.originGridPlus[row][col] = 1
            elif mode == 'x' :
                self.originGridX[row][col] = 1
            elif mode == 'o' :
                self.originGridPlus[row][col] = 1
                self.originGridX[row][col] = 1

        self.gridX = []
        self.gridPlus = []
        for i in range(self.N) :
            self.gridX.append([])
            self.gridPlus.append([])
            for j in range(self.N) :
                self.gridX[-1].append(self.originGridX[i][j])
                self.gridPlus[-1].append(self.originGridPlus[i][j])

        self.putX()
        self.putPlus()
        self.getResult()

    def putX(self) :
        freeRow = [True for _ in range(self.N)]
        freeCol = [True for _ in range(self.N)]
        for row in range(self.N) :
            for col in range(self.N) :
                if self.gridX[row][col] :
                    freeRow[row] = False
                    freeCol[col] = False

        for row in range(self.N) :
            if freeRow[row] :
                for col in range(self.N) :
                    if freeCol[col] :
                        self.gridX[row][col] = 1
                        freeRow[row] = False
                        freeCol[col] = False
                        break;

    def putPlus(self) :
        dia1 = [set() for _ in range(self.N * 2 - 1)]
        dia2 = [set() for _ in range(self.N * 2 - 1)]
        available = set()
        for row in range(self.N) :
            for col in range(self.N) :
                d1, d2 = self.diaIndex(row, col)
                dia1[d1].add((row, col))
                dia2[d2].add((row, col))
                available.add((row, col))

        for row in range(self.N) :
            for col in range(self.N) :
                if self.gridPlus[row][col] :
                    self.place(row, col, dia1, dia2, available)

        while len(available) :
            total = self.N * self.N + 1
            for row, col in available :
                d1, d2 = self.diaIndex(row, col)
                tmpTotal = len(dia1[d1]) + len(dia2[d2]) - 2
                if tmpTotal < total :
                    total = tmpTotal
                    targetRow = row
                    targetCol = col
            self.gridPlus[targetRow][targetCol] = 1
            self.place(targetRow, targetCol, dia1, dia2, available)

    def place(self, row, col, dia1, dia2, available) :
        d1, d2 = self.diaIndex(row, col)
        cells = []
        for cell in dia1[d1] :
            cells.append(cell)
        for cell in dia2[d2] :
            cells.append(cell)

        for cell in cells :
            if cell in available :
                available.remove(cell)
            cd1, cd2 = self.diaIndex(cell[0], cell[1])
            if cell in dia1[cd1] :
                dia1[cd1].remove(cell)
            if cell in dia2[cd2] :
                dia2[cd2].remove(cell)

    def getResult(self) :
        self.modify = []
        self.score = 0
        for row in range(self.N) :
            for col in range(self.N) :
                if self.originGridX[row][col] and self.originGridPlus[row][col] :
                    oriMode = 'o'
                elif self.originGridX[row][col] :
                    oriMode = 'x'
                elif self.originGridPlus[row][col] :
                    oriMode = '+'
                else :
                    oriMode = '.'

                if self.gridX[row][col] and self.gridPlus[row][col] :
                    mode = 'o'
                elif self.gridX[row][col] :
                    mode = 'x'
                elif self.gridPlus[row][col] :
                    mode = '+'
                else :
                    mode = '.'

                if mode == '+' or mode == 'o' :
                    self.score += 1
                if mode == 'x' or mode == 'o' :
                    self.score += 1
                if mode != oriMode :
                    self.modify.append((mode, row + 1, col + 1))

    def diaIndex(self, row, col) :
        return (row + col, row + (self.N - 1 - col))
                
    def output(self, caseIndex) :
        stdout.write("Case #%d: %d %d\n" % (caseIndex, self.score, len(self.modify)))
        for modify in self.modify :
            stdout.write("%s %d %d\n" % modify)

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

