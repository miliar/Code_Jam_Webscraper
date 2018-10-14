#!/usr/bin/env python

import sys;
class watershed:
    def __init__(self, grid):
        self.grid = grid
        self.out = []
        self.dir = []
        self.sinks = []
        
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
    
    def parse(self):
        rows = self.rows
        cols = self.cols
        
        self.out = [[ None for c in range(cols)] for r in range(rows)]
        self.dir = [[ None for c in range(cols)] for r in range(rows)]
        
        ch = 'a'
        self.out[0][0] = ch
        
        self.sinks = []
        
        for row in range(rows):
            for col in range(cols):
                low = None
                val = self.grid[row][col]
                d = None
                
                if row > 0:
                    if self.grid[row-1][col] < val:
                        val = self.grid[row - 1][col]
                        low = (row-1, col)
                        d = 'u'
                if col > 0:
                    if self.grid[row][col-1] < val:
                        val = self.grid[row][col-1]
                        low = (row, col-1)
                        d = 'l'
                if col < cols - 1:
                    if self.grid[row][col+1] < val:
                        val = self.grid[row][col+1]
                        low = (row, col+1)
                        d = 'r'
                if row < rows - 1:
                    if self.grid[row+1][col] < val:
                        val = self.grid[row+1][col]
                        low = (row+1, col)
                        d = 'd'
                        
                if low == None:
                    self.sinks.append((row, col))
                else:
                    self.dir[row][col] = d
        
        
        if self.sinks[0] != (0, 0):
            self.findFirstSink(0, 0)
        
        print self.sinks
        
        self.markFromSinks()
        
        res = ''
        for row in self.out:
            for col in row:
                if col == None:
                    res += 'x '
                else:
                    res += col + ' '
            res += '\n'
        return res
    
    def markFromSinks(self):
        ch = 'a'
        for (row, col) in self.sinks:
            self.mark(row, col, ch)
            ch = chr(ord(ch)+1)
    
    def mark(self, row, col, ch):
        self.out[row][col] = ch
        
        if row < self.rows - 1 and self.dir[row+1][col] == 'u':
            self.mark(row+1, col, ch)
                        
        if row > 0 and self.dir[row-1][col] == 'd':
            self.mark(row-1, col, ch)
            
        if col < self.cols - 1 and self.dir[row][col+1] == 'l':
            self.mark(row, col+1, ch)
            
        if col > 0 and self.dir[row][col-1] == 'r':
            self.mark(row, col-1, ch)
    
    def findFirstSink(self, row, col):
        if (row, col) in self.sinks:
            self.out[row][col] = 'a'
            self.sinks.remove((row, col))
            self.sinks = [(row, col)] + self.sinks
            return
        
        if self.dir[row][col] == 'u':
            row -= 1
        if self.dir[row][col] == 'd':
            row += 1
        if self.dir[row][col] == 'l':
            col -= 1
        if self.dir[row][col] == 'r':
            col += 1
            
        return self.findFirstSink(row, col)
        

if __name__ == '__main__':
    name = sys.argv[1]
    
    file = open(name)
    
    cases = int(file.readline())
    results = []
    
    for case in range(cases):
        line = file.readline().strip().split(' ')
        (h, w) = (int(line[0]), int(line[1]))
        
        grid = []
        for i in range(h):
            grid.append([int(val) for val in file.readline().strip().split(' ')])
        
        results.append('Case #%d:\n%s' % (case + 1, watershed(grid).parse()))
    
    
    file.close()
    
    file = open(name.replace('.in', '.out'), 'w')
    
    for result in results:
        print result
        file.write(result)
        #file.write('\n')
    
    file.close()