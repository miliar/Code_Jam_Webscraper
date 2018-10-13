#!/usr/bin/python

import fileinput, math

class Case(object):
    casenum = 0
    board = None
    finalboard = None
    solution = ""
    
    def __init__(self, casenum, board):
        self.casenum = casenum
        self.finalboard = board
        
        self.board = []
        for i in self.finalboard:
            self.board.append([])
            for j in i:
                self.board[len(self.board) - 1].append(100)
                
        
    def solve(self):
        maxheight = 1
        for y in self.finalboard:
            for x in y:
                if x > maxheight:
                    maxheight = x
        self.mowall(maxheight)
        
        for h in range(maxheight - 1, 0, -1):
            for r in range(0, len(self.board)):
                if self.row_lte(h, r): self.mow_row(h, r)
            for c in range(0, len(self.board[0])):
                if self.col_lte(h, c): self.mow_col(h, c)
        
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if not self.board[i][j] == self.finalboard[i][j]:
                    self.solution = "NO"
                    return self.solution
        self.solution = "YES"
        return self.solution
                    
    def mowall(self, height):
        for r in range(0, len(self.board)):
            self.mow_row(height, r)
        
    def mow_row(self, height, row):
        for c in range(0, len(self.board[row])):
            if self.board[row][c] > height: self.board[row][c] = height
        
    def mow_col(self, height, col):
        for r in range(0, len(self.board)):
            if self.board[r][col] > height: self.board[r][col] = height
   
    def row_lte(self, height, row):
        for c in range(0, len(self.board[row])):
            if self.finalboard[row][c] > height: return False
        return True
        
    def col_lte(self, height, col):
        for r in range(0, len(self.board)):
            if self.finalboard[r][col] > height: return False
        return True 
    
    def __str__(self):
        if not self.solution:
            self.solve()
        #print self.board
        return "Case #%i: %s" % (self.casenum, self.solution)
        
if __name__ == "__main__":
    firstline = True
    cases = []
    curboard = []
    linesforcase = 0
    
    for line in fileinput.input():
        if firstline:
            firstline = False
            continue
        if linesforcase == 0:
            bounds = line.split()
            linesforcase = int(bounds[0])
            curboard = []
        else:
            
            linesplit = line.split()
            curboard.append([])
            for s in linesplit:
                curboard[len(curboard) - 1].append(int(s))
            linesforcase -= 1
            
            if linesforcase == 0:
                cases.append(Case(len(cases) + 1, curboard))
            
    for case in cases:
        print case
        
