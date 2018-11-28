"""
Kamal Wood
Tuesday, 2 September 2009
Google Code Jam 2009
Qualification Round
B. Watersheds
"""

class Cell:
    def __init__(self, alt):
        self.alt = alt # The cell's altitude
        self.neighbours = {'N': None, 'W': None, 'E': None, 'S': None} # The cell's neighbours
        self.sink = None # The cell that this cell drains into
        self.basin = '' # The basin the cell belongs to.

    def getLowest(self):
        neighbours = {'N': self.alt + 1, 'W': self.alt+1, 'E': self.alt+1, 'S': self.alt+1}
        if self.neighbours['N'] != None:
            neighbours['N'] = self.neighbours['N'].alt
        if self.neighbours['W'] != None:
            neighbours['W'] = self.neighbours['W'].alt
        if self.neighbours['E'] != None:
            neighbours['E'] = self.neighbours['E'].alt
        if self.neighbours['S'] != None:
            neighbours['S'] = self.neighbours['S'].alt

        lowest = self

        if neighbours['N'] < lowest.alt:
            lowest = self.neighbours['N']
        if neighbours['W'] < lowest.alt:
            lowest = self.neighbours['W']
        if neighbours['E'] < lowest.alt:
            lowest = self.neighbours['E']
        if neighbours['S'] < lowest.alt:
            lowest = self.neighbours['S']

        return lowest

class Map:
    def __init__(self, height, width):
        self.grid = []
        self.height = height
        self.width = width

    def addRow(self, altList):
        row = []
        for alt in altList:
            row.append(Cell(int(alt)))
        self.grid.append(row)

    ## Assigns neighbours.
    def setNeighbours(self):
        row = 0
        while row < self.height:
            col = 0
            while col < self.width:
                if row - 1 >= 0:
                    self.grid[row][col].neighbours['N'] = self.grid[row-1][col]
                if col - 1 >= 0:
                    self.grid[row][col].neighbours['W'] = self.grid[row][col-1]
                if col + 1 < self.width:
                    self.grid[row][col].neighbours['E'] = self.grid[row][col+1]
                if row + 1 < self.height:
                    self.grid[row][col].neighbours['S'] = self.grid[row+1][col]
                col += 1
            row += 1

    def solve(self):
        first = self.grid[0][0]
        current = first
        while current != current.getLowest():
            current = current.getLowest()
        current.sink = current
        first.sink = current
        current.basin = 'a'
        first.basin = 'a'

        letters = "abcdefghijklmnopqrstuvwxyz"
        loc = 1
        for row in self.grid:
            for cell in row:
                if cell == first or cell.basin != '':
                    continue

                current = cell
                while current != current.getLowest():
                    current = current.getLowest()
                cell.sink = current
                ## If you've found a new sink then you've found a new basin, so label it with a new letter.
                if current.basin == '':
                    current.sink = current
                    current.basin = letters[loc]
                    loc += 1
                cell.basin = current.basin

        return self.stringify()

    def stringify(self):
        result = []
        for row in self.grid:
            line = ""
            for cell in row:
                line = line + cell.basin + ' '
            line = line[:-1] # Cuts off the trailing space.
            result.append(line)
        return result

def main():
    outFile = open("B-large-OUTPUT.out","w")
    with open("B-large.in","r") as inFile:
        numMaps = int(inFile.readline())
        N = 1

        while N <= numMaps:
            line = inFile.readline().split()
            height = int(line[0])
            width = int(line[1])
            grid = Map(height, width)
            count = 0

            while count < height:
                line = inFile.readline().split()
                grid.addRow(line)
                count += 1

            grid.setNeighbours()
            result = grid.solve()

            outFile.write("Case #" + str(N) + ":\n")
            for line in result:
                outFile.write(line)
                outFile.write("\n")
            N += 1

    outFile.close()

main()




