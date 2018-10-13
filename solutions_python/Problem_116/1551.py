#!/usr/bin/python

import fileinput, math

class Chain(object):
    items = None
    character = None
    dx = 0
    dy = 0
    
    def __init__(self, character, dx, dy):
        self.character = character
        self.items = []
        self.dx = dx
        self.dy = dy
        
    def add(self, char, x, y):
        if self.character == "T":
            self.character = char
        if char == self.character or char == "T":
            if len(self.items) == 0:
                self.items.append((x, y))
            #elif len(self.items) == 1:
            #    dx = math.fabs(x - self.items[len(self.items) - 1][0])
            #    dy = math.fabs(y - self.items[len(self.items) - 1][1])
            #    if dx <= 1 and dy <= 1 and dx + dy <= 2:
            #        self.items.append((x, y))
            else:
                #dx = self.items[1][0] - self.items[0][0]
                #dy = self.items[1][1] - self.items[0][1]
                if self.items[len(self.items) - 1][0] + self.dx == x and self.items[len(self.items) - 1][1] + self.dy == y:
                    self.items.append((x, y))
        
    def finished(self):
        return len(self.items) >= 4
        
    def __str__(self):
        strep = ["    ", "    ", "    ", "    "]
        for i in self.items:
            strep[i[1]] = strep[i[1]][:i[0]] + self.character + strep[i[1]][i[0] + 1:]
        return strep[0] + "\n" + strep[1] + "\n" + strep[2] + "\n" + strep[3]
    

class Case(object):
    casenum = 0
    board = None
    
    solution = -1
    
    def __init__(self, casenum, board):
        self.casenum = casenum
        self.board = board
        
    def solve(self):
        chains = []
        allfilled = True
        for y in range(0, len(self.board)):
            for x in range(0, len(self.board[y])):
                if self.board[y][x] != ".":
                    if x < len(self.board[y]) - 1: 
                        chains.append(Chain(self.board[y][x], 1, 0))
                        if y < len(self.board) - 1:
                            chains.append(Chain(self.board[y][x], 1, 1))
                    if x > 0 and y < len(self.board) - 1:
                        chains.append(Chain(self.board[y][x], -1, 1))
                    if y < len(self.board) - 1:
                        chains.append(Chain(self.board[y][x], 0, 1))

                    for c in chains:
                        c.add(self.board[y][x], x, y)
                        if c.finished():
                            if c.character == "X":
                                self.solution = 1
                                return
                            else:
                                self.solution = 2
                                return
                else:
                    allfilled = False
        if allfilled:
            self.solution = 3
        else:
            self.solution = 0
        
            
            
    def __str__(self):
        if self.solution == -1:
            self.solve()
        
        answer = "Game has not completed"
        if self.solution == 1:
            answer = "X won"
        elif self.solution == 2:
            answer = "O won"
        elif self.solution == 3:
            answer = "Draw"
        
        return "Case #%i: %s" % (self.casenum, answer)
        
if __name__ == "__main__":
    firstline = True
    cases = []
    curboard = []
    
    for line in fileinput.input():
        if firstline:
            firstline = False
            continue
        if line == "\n":
            cases.append(Case(len(cases) + 1, curboard)) # finish the case
            curboard = []
        else:
            curboard.append(line[:len(line)-1])
    if len(curboard):
        cases.append(Case(len(cases) + 1, curboard)) # finish the case  
            
    for case in cases:
        print case
