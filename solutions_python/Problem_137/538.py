from itertools import permutations
import fileinput
import sys
sys.setrecursionlimit(100000000)

class Board:
    width = 0
    height = 0
    num_mines = 0
    num_squares = 0
    board_string = []

    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board_string = []

        #self.width, self.height, self.num_mines, self.num_squares = self.extract_squares()

        # Build board string
        for i in range(self.num_mines):
            self.board_string.append('*')
        while len(self.board_string) < self.width*self.height:
            self.board_string.append('.')

    def index(self, x, y):
        return self.width*y + x

    def coords(self, index):
        x = index % y*x
        y = (index - x) / x
        return x, y

    def num_for_square(self, x, y):
        return (x-1)*2 + (y-1)*2

    def extract_squares(self):
        x = self.width
        y = self.height
        total = 0
        num_squares = 0

        while self.num_for_square(x, y) + total < self.num_mines:
            total += self.num_for_square(x, y)
            x -= 2
            y -= 2
            num_squares += 1

        return x, y, self.num_mines - total, num_squares

    def check_space(self, x, y):
        if (x >= self.width or x < 0):
            return False
        if (y >= self.height or y < 0):
            return False
        if (not self.board_string[self.index(x,y)] == '.'):
            return False
        if (not self.check_mine(x, y)):
            self.board_string[self.index(x, y)] = str(self.mine_neighbors(x, y))
            if (self.mine_neighbors(x, y) == 0):
                self.check_space(x-1, y-1)
                self.check_space(x-1, y)
                self.check_space(x-1, y+1)
                self.check_space(x, y-1)
                self.check_space(x, y)
                self.check_space(x, y+1)
                self.check_space(x+1, y-1)
                self.check_space(x+1, y)
                self.check_space(x+1, y+1)

    def check_solution(self):
        for i in range(len(self.board_string)):
            if self.board_string[i] == '.':
                return False
        return True

    def find_solution(self):
        original_board = self.board_string[:]
        for i in range(self.width):
            for j in range(self.height):
                self.check_space(i, j)
                if (self.check_solution()):
                    self.board_string = original_board[:]
                    self.board_string[self.index(i, j)] = 'c'
                    return True
                self.board_string = original_board[:]
        return False

    def solve(self):
        # Permute board
        perms = perm_unique(self.board_string)
        for b in perms:
            self.board_string = list(b)
            if(self.find_solution()):
                return str(self).strip()
        return 'Impossible'

    def mine_neighbors(self, x, y):
        neighbors = 0
        if self.check_mine(x-1, y-1):
            neighbors += 1
        if self.check_mine(x-1, y):
            neighbors += 1
        if self.check_mine(x-1, y+1):
            neighbors += 1
        if self.check_mine(x, y-1):
            neighbors += 1
        if self.check_mine(x, y):
            neighbors += 1
        if self.check_mine(x, y+1):
            neighbors += 1
        if self.check_mine(x+1, y-1):
            neighbors += 1
        if self.check_mine(x+1, y):
            neighbors += 1
        if self.check_mine(x+1, y+1):
            neighbors += 1

        return neighbors

    def check_mine(self, x, y):
        # Check bounds
        if x >= self.width:
            return False
        if y >= self.height:
            return False
        if x < 0:
            return False
        if y < 0:
            return False

        # Check tile
        index = self.index(x, y)
        if (self.board_string[index] == '*'):
            return True
        else:
            return False

    def __repr__(self):
        string = ''
        for i in range(self.num_squares*2):
            for j in range(self.width + self.num_squares*2):
                string += '*'
            string += '\n'

        for j in range(self.height):
            for k in range(self.num_squares):
                string += '**'
            for i in range(self.width):
                string += self.board_string[self.index(i, j)]
            string += '\n'

        return string

class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

num_inputs = 0
lines = []

for line in fileinput.input():
    lines.append(line)

num_inputs = int(lines[0])

for i in range(1,num_inputs+1):
    board = Board(int(lines[i].split(' ')[1]), int(lines[i].split(' ')[0]), int(lines[i].split(' ')[2]))
    print("Case #"+str(i)+':\n'+board.solve())