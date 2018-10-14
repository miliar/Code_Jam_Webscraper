# Problem from Google Code Jam 2009

# Store sources for each cell.  Determine sinks.  Allocate lables to sinks.
# Propagate labels to sources.
import sys

class Cell:
    rows = 0
    cols = 0
    def __init__(self, row, col, elevation):
        self.row = row
        self.col = col
        self.elevation = int(elevation)
        self.sources = []
        self.sink = False
    def findNeighbors(self):
        # Add north
        self.neighbors = []
        if self.row > 0:
            self.neighbors += [c for c in cells if c.row == self.row-1 and c.col == self.col]
        # Add west
        if self.col > 0:
            self.neighbors += [c for c in cells if c.row == self.row and c.col == self.col-1]
        # Add east
        if self.col < self.cols-1:
            self.neighbors += [c for c in cells if c.row == self.row and c.col == self.col+1]
        # Add south
        if self.row < self.rows-1:
            self.neighbors += [c for c in cells if c.row == self.row+1 and c.col == self.col]
    def __cmp__(self, other):
        if self.elevation != other.elevation:
            return self.elevation - other.elevation
        elif self.row != other.row:
            return self.row - other.row # north wins, west&east beat south
        else:
            return self.col - other.col # west beats east

def flow():
    
    for c in cells:
        # Find the cell's sink, and tell the sink that we're a source.
        c.findNeighbors()
        if c.neighbors:
            low = min(c.neighbors)
            if low.elevation < c.elevation:
                low.sources.append(c)
            else:
                # Nobody lower, so we're a sink
                c.sink = True
        else:
            c.sink = True
    label = 0
    for c in cells:
        if c.sink:
            propagateLabel(c, label)
            label += 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for c in cells:
        oldlabel = c.label
        if isinstance(oldlabel, int):
            for c2 in cells:
                if c2.label == oldlabel:
                    c2.label = alphabet[0]
            alphabet = alphabet[1:]
            
def propagateLabel(cell, label):
    cell.label = label
    map(propagateLabel, cell.sources, [label]*len(cell.sources))

file = open(sys.argv[1])
numCases = int(file.readline())
for case in range(1, numCases+1):
    (Cell.rows, Cell.cols) = map(int, file.readline().split())
    cells = []
    for row in range(Cell.rows):
        elevations = file.readline().split()
        for col in range(Cell.cols):
            cells.append(Cell(row, col, elevations[col]))
    flow()
    print 'Case #%d:' % case
    for r in range(Cell.rows):
        print ' '.join([c.label for c in cells[r*Cell.cols:r*Cell.cols+Cell.cols]])

