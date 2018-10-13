import string
import copy

class Point:
    def __init__(self, i, j, height):
        self.i = i
        self.j = j
        self.height = height
        self.label = ''
        self.flows_from = copy.deepcopy([])
        self.is_sink = False
        self.basin = []

    def __cmp__(self, other):
        return self.height - other.height

    def __str__(self):
        return "Point at (%d, %d) and altitude %d\n" % (self.i, self.j, self.height)

    def __repr__(self):
        return self.__str__()

    def update(self, a_map):
        directions = (lambda i, j: (a_map[i-1][j], 'A(NORTH)'),
                  lambda i, j: (a_map[i][j-1], 'B(WEST)'),
                  lambda i, j: (a_map[i][j+1], 'C(EAST)'),
                  lambda i, j: (a_map[i+1][j], 'D(EAST)'))
        neighbours = [dir(self.i, self.j) for dir in directions]
        neighbours = [neighbour for neighbour in neighbours if neighbour[0] is not None]
        if neighbours:
            best_neighbour = min(neighbours)[0]
            if best_neighbour.height < self.height:
                best_neighbour.flows_from.append(self)
            else:
                self.is_sink = True
        else:
            self.is_sink = True

    def get_drainage_basin(self):
        if self.basin:
            return self.basin
        else:
            self.basin = []
            self.basin.append(self)
            for p in self.flows_from:
                self.basin += p.get_drainage_basin()
            return self.basin

def process_input():    
    t = int(raw_input())
    maps = []
    for i in range(t):
        next_map = []
        hw = [int(i) for i in raw_input().split()]
        h, w = hw[0], hw[1]
        for j in range(h):
            next_map.append([int(s) for s in raw_input().split()])
        maps.append(next_map)
    return maps

def get_drainage_basins(a_map):
    m = len(a_map)
    n = len(a_map[0])
    a_map = [[Point(i+1, j+1, a_map[i][j]) for  j in range(n)] for i in range(m)]
    a_map.insert(0, [None for i in range(n+2)])
    a_map.append([None for i in range(n+2)])
    for row in a_map:
        row.insert(0, None)
        row.append(None)
    m += 2
    n += 2
    for i in range(1, m-1):
        for j in range(1, n-1):
            a_map[i][j].update(a_map)
    pts = [a_map[i][j] for i in range(1, m-1) for j in range(1, n-1)]
    sinks = [pt for pt in pts if pt.is_sink]
    sinks.sort(key=lambda s: min([p.i*m+p.j for p in s.get_drainage_basin()]))
    res = [['a' for i in range(n-2)]for j in range(m-2)]
    symbols = string.ascii_lowercase
    curr_symbol = 0
    for s in sinks:
        for p in s.get_drainage_basin():
            res[p.i-1][p.j-1] = symbols[curr_symbol]
        curr_symbol += 1
    return res

if __name__ == "__main__":
    the_maps = process_input()
    i = 0
    for each_map in the_maps:
        drainage_basin = get_drainage_basins(each_map)
        print "Case #%d:" % (i+1)
        print "\n".join([" ".join(row) for row in drainage_basin])
        i += 1
        
