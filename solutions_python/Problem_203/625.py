import numpy as np
import math
import Queue

class Q1:
    def processFile(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0

        self.numCases = int(raw_input())  # read a line with a single integer

        for i in xrange(1, self.numCases + 1):
            row, column = map(int, raw_input().split())  # read a list of integers, 2 in this case
            grid = []
            for _ in range(row):
                grid.append(list(raw_input()))

            newGrid = self.process(row, column, grid)
            print "Case #{}:\n{}".format(i, self.gridString(newGrid))

    def gridString(self, grid):
        # New grid string
        newGrid = ''
        for rowString in grid:
            newGrid += ''.join(rowString) + '\n'
        newGrid = newGrid[0: len(newGrid) - 1]
        return newGrid

    def run(self):
        self.processFile()

    def process(self, rows, columns, grid):
        recurse = False
        # Check rows
        sumRows = [0] * columns
        for row in range(rows):
            for columnIndex in range(columns):
                sumRows[columnIndex] += ord(grid[row][columnIndex])

        # print grid
        # print sumRows, ord('?') * rows

        fillHorizontally = False
        if ord('?') * rows in sumRows:
            fillHorizontally = True
        else:
            grid = map(list, zip(*grid))
            rows, columns = (columns, rows)

        # Fill horizontally
        for row in range(rows):
           # Find first character
            searchColumn = 1
            rowCharacter = grid[row][0]
            while rowCharacter == '?' and searchColumn < columns:
                # print grid
                # print searchColumn, columns
                rowCharacter = grid[row][searchColumn]
                searchColumn += 1

            if rowCharacter == '?':
                recurse = True
                continue

            for column in range(columns):
                if grid[row][column] == '?':
                    grid[row][column] = rowCharacter
                else:
                    rowCharacter = grid[row][column]

        if fillHorizontally == False:
            grid = map(list, zip(*grid))

        if recurse:
            grid = self.process(rows, columns, grid)

        return grid


def main():
    q1 = Q1()
    q1.run()


if  __name__ =='__main__':
    main()
