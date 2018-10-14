import sys
from copy import deepcopy

class Tile:
    def __init__(self):
        self.revealed=False
        self.visited=False
        self.clicked=False
        self.highlight=False
    def __str__(self):
        if self.highlight:
            return '@'
        if self.clicked:
            return 'c'
        if self.revealed:
            return '.'
        return '*'

class Grid:
    def __init__(self, R, C, target_revealed):
        self.size_x = C
        self.size_y = R
        self.data = [ [Tile() for i in range(C)] for i in range(R) ]
        self.open_list=[]
        self.target_revealed = target_revealed
        self.num_revealed = 0
    def all_adjacent(self, x, y):
        pairs = [ (x-1,y-1), (x+0,y-1), (x+1, y-1),
                  (x-1,y+0),            (x+1, y+0),
                  (x-1,y+1), (x+0,y+1), (x+1, y+1)
                  ]
        for i, j in pairs:
            if self.valid(i, j):
                yield i,j
    def valid(self, x, y):
        return x >= 0 and x < self.size_x and y >= 0 and y < self.size_y
    def get(self, x, y):
        return self.data[y][x]
    def __str__(self):
        s = ""
        for y in range(self.size_y):
            if y != 0:
                s += "\n"
            for x in range(self.size_x):
                s += str(self.get(x,y))
        return s
    def add_to_open(self, x, y):
        self.open_list.append( (x,y) )
    def pop_open(self, max_to_reveal):
        if self.has_open(max_to_reveal):
            return self.open_list.pop(0)
        return None
    def has_open(self,max_to_reveal):
        while len(self.open_list) > 0:
            x,y = self.open_list[0]
            num_revealed = 0
            for i,j in self.all_adjacent(x,y):
                if not self.get(i,j).revealed:
                    num_revealed += 1
            if num_revealed <= max_to_reveal:
                return True
            else:
                self.open_list.pop(0)
        return False
    def mark_revealed(self,x,y):
        if not self.get(x,y).revealed:
            self.get(x,y).revealed=True
            self.num_revealed += 1
    def target_reached(self):
        return self.num_revealed == self.target_revealed
    def target_exceeded(self):
        return self.num_revealed > self.target_revealed
    def get_adjacent(self, x, y):
        return [ (i,j) for i,j in self.all_adjacent(x,y)]
    def mark_adjacent_revealed(self,x,y):
        for i,j in self.all_adjacent(x,y):
            self.mark_revealed(i,j)

# reveal x,y and if it is empty recursively reveal 
def recurse(grid, x, y, depth):
    # print("recurse", depth, "-", x, y)
    grid.mark_revealed(x,y)
    unrevealed_adjs = [ (i,j) for i,j in grid.get_adjacent(x,y) if not grid.get(i,j).revealed ]
    grid.mark_adjacent_revealed(x,y)
    if grid.target_reached():
        # print("target reached")
        return grid
    if grid.target_exceeded():
        # print("target exceeded")
        return None
    for adj in unrevealed_adjs:
        i, j = adj
        new_grid = deepcopy(grid)
        res = recurse(new_grid, i, j, depth+1)
        if res is not None and res.target_reached():
            # print(res)
            return res
    return None

def test(R,C,M):
    num_white = R*C - M
    grid = Grid(R, C, num_white)
    grid.get(0,0).clicked = True
    grid.mark_revealed(0,0)
    if grid.target_reached():
        return grid
    res = recurse(grid, 0, 0, 0)
    if res is not None:
        return res
    else:
        return None

def main(argv):
    if len(argv) < 2:
        while True:
            print("")
            print("Next question:")
            R,C,M = [ int(val) for val in sys.stdin.readline().split() ]
            res = test(R,C,M)
            if res is None:
                print("Impossible")
            else:
                print("Solved")
                print(str(res))
    else:
        filename = argv[1]
        with open(filename) as f:
            num_tests = int(f.readline())
            for i in range(num_tests):
                R, C, M = [ int(val) for val in f.readline().split() ]
                res = test(R,C,M)
                print( "Case #", i+1, ":", sep='')
                if res is None:
                    print("Impossible")
                else:
                    print(str(res))
if __name__ == "__main__":
    main(sys.argv)