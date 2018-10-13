#!/usr/bin/env python
from pprint import pprint

class Watersheds(object):
    def __init__(self,filename):
        with open(filename) as f:
            state = 'first'
            
            for line in f.readlines():
                line = line.strip()
                if state == 'first':
                    self.map_count = int(line)
                    self.maps = []
                    state = 'dim'

                elif state == 'dim':
                    dim = line.split(' ')
#                    print dim

                    cur_map = Map(int(dim[0]),int(dim[1]))
                    self.maps.append(cur_map)

                    state = 'map'
                    row = 0
                    
                elif state == 'map':
                    cur_map.set_row(row,line.split(' '))
                    
                    row += 1
                    if row == cur_map.rows:
                        state = 'dim'
                    
    def solve(self):
        case = 0
        for map in self.maps:
            case += 1
            print 'Case #%s:' % case
            map.solve()
            map.print_codes()

class Point(object):
    def __init__(self,elevation,row,col):
        self.elevation = elevation
        self.row = row
        self.col = col
        self.direction = ''
        self.target = None
        self.sources = []
        self.basin = -1
        self.code = ''
    
    def __repr__(self):
        return '%s%s(%s %s)' % (self.elevation,self.direction,self.basin,self.code)
        
class Map(object):
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        
        self.grid = []
        for i in xrange(rows):
            self.grid.append([])
            
        self.basin_codes = []
        self.available_codes = 'abcdefghijklmnopqrstuvwxyz'

    def set_row(self,row,cols):
        self.grid[row] = []
        i=0
        for col in cols:
            self.grid[row].append(Point(col,row,i))
            i+=1
        
    def print_grid(self):
        for row in self.grid:
            for col in row:
                print col,
            print
            
    def solve(self):
        sinks = []
        for i in xrange(self.rows):
            for j in xrange(self.cols):
                elevation = self.grid[i][j].elevation

                target = None
                low = elevation
                direction = 'x'
                
                north = None
                west = None
                east = None
                south = None
                
                if i > 0:
                    north = self.grid[i-1][j]
                if j > 0:
                    west = self.grid[i][j-1]
                if j < self.cols-1:
                    east = self.grid[i][j+1]
                if i < self.rows-1:
                    south = self.grid[i+1][j]
                
                if north and north.elevation < low:
                    target = north
                    low = north.elevation
                    direction = '^'
                if west and west.elevation < low:
                    target = west
                    low = west.elevation
                    direction = '<'
                if east and east.elevation < low:
                    target = east
                    low = east.elevation
                    direction = '>'
                if south and south.elevation < low:
                    target = south
                    low = south.elevation
                    direction = 'v'
                    
                self.grid[i][j].direction = direction
                self.grid[i][j].target = target

                if target:
                    target.sources.append(self.grid[i][j])
                else:
                    sinks.append(self.grid[i][j])
        
        basin = 0
        self.basin_codes.append('')
        for sink in sinks:
            basin += 1
            self.populate_basin(sink,basin)
            self.basin_codes.append('')

        for i in xrange(self.rows):
            for j in xrange(self.cols):
                point = self.grid[i][j]
                if not self.basin_codes[point.basin]:
                    self.basin_codes[point.basin] = self.available_codes[0]
                    self.available_codes = self.available_codes[1:]
                point.code = self.basin_codes[point.basin]
    
                
        #self.print_grid()
        #print         
    def print_codes(self):
        for row in self.grid:
            for col in row:
                print col.code,
            print
        
    def populate_basin(self,root,basin_number):
        root.basin = basin_number
        for source in root.sources:
            self.populate_basin(source,basin_number)
        
if __name__ == '__main__':
    import sys
    Watersheds(sys.argv[1]).solve()