def print_result(i, result):
    print 'Case #%s: %s' % (i+1, result)

def debug(*args):
    # print ' '.join(map(str, args))
    pass

# cell moving functions
def get_added_cell(cell, direction):
    x, y = cell
    if direction == 0:
        return (x, y+1)
    elif direction == 1:
        return (x+1, y)
    elif direction == 2:
        return (x, y-1)
    elif direction == 3:
        return (x-1 , y)

def move_cell(cell, dx, dy):
    x, y = cell
    return (x+dx, y+dy)

def rotate_cell(mino, times = 1):
    "rotate cell's place clockwise"
    x, y = mino
    if times % 4 == 0:
        return x, y
    if times % 4 == 1:
        return y, -x
    elif times % 4 == 2:
        return -x, -y
    elif times % 4 == 3:
        return -y, x

def mirror_cell(mino, axis='y'):
    "swap cell's x coordinate"
    x, y = mino
    if axis == 'y':
        return -x, y
    else:
        return x, -y

def try_make_mino(places, directions):
    cells = [(0,0)]          # list of (x,y)
    for destination, direction in zip(places, directions):
        added = get_added_cell(cells[destination], direction)
        if added in cells:
            return None
        cells.append(added)
    return X_omino(set(cells))

def normalize_cells(cells):
    """make minimum x and y coordinates to zero"""
    min_x = min([x for x, y in cells])
    min_y = min([y for x, y in cells])
    return set([(x-min_x, y-min_y) for x, y in cells])

class X_omino(object):
    def __init__(self, cells):
        self.cells = normalize_cells(cells)
    def printout(self):        
        for y in range(max([y_ for x_, y_ in self.cells]), -1, -1):
            for x in range(max([x_ for x_, y_ in self.cells])+1):
                if (x, y) in self.cells:
                    print 'O',
                else:
                    print ' ',
            print

    def __str__(self):
        rows = []
        for y in range(max([y_ for x_, y_ in self.cells]), -1, -1):
            row = ''
            for x in range(max([x_ for x_, y_ in self.cells])+1):
                if (x, y) in self.cells:
                    row += 'O'
                else:
                    row += ' '
            rows.append(row)
        return '\n'.join(rows)
            
    def rotate(self, times = 1):
        return X_omino(set(map(lambda c:rotate_cell(c, times),self.cells)))
    def mirror(self, axis = 'y'):
        return X_omino(set(map(lambda c:mirror_cell(c, axis),self.cells)))
        
    def __eq__(self, other):
        tmp = self
        if tmp.cells == other.cells: return True
        tmp = tmp.rotate()
        if tmp.cells == other.cells: return True
        tmp = tmp.rotate()
        if tmp.cells == other.cells: return True
        tmp = tmp.rotate()
        if tmp.cells == other.cells: return True

        tmp = self.mirror()
        if tmp.cells == other.cells: return True
        tmp = tmp.rotate()
        if tmp.cells == other.cells: return True
        tmp = tmp.rotate()
        if tmp.cells == other.cells: return True
        tmp = tmp.rotate()
        if tmp.cells == other.cells: return True
        return 

# helper routines for generating X-omino
def gen_directions(X):
    for i in xrange(4**(X-1)):
        tmp = i
        result = []
        for j in xrange(X-1):
            result.append(tmp%4)
            tmp /= 4
        yield result

def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)

def gen_places(X):
    for i in xrange(fac(X-1)):
        tmp = i
        result = []
        for j in xrange(X-1):
            result.append(tmp%(j+1))
            tmp/=(j+1)
        yield result

def gen_Xomino(X):
    Xominos = []

    for places in gen_places(X):
        for directions in gen_directions(X):
            mino = try_make_mino(places, directions)
            if mino and mino not in Xominos:
                Xominos.append(mino)
                yield mino

def check(X, R, C):
    if (R*C)%X != 0:
        debug('R*C not multiple of X')
        return False
    return True

class board(object):
    def __init__(self, R, C, cells = None):
        self.R = R
        self.C = C
        if cells:
            self.cells = set(cells.copy())
        else:
            self.cells = set()
    def place_mino(self, mino, dx, dy):
        max_x = max([x for x, y in mino.cells])
        max_y = max([y for x, y in mino.cells])
        placed = map(lambda c:move_cell(c, dx, dy), mino.cells)
        if (self.cells.isdisjoint(placed) and
            0 <= dx and max_x + dx < self.C and
            0 <= dy and max_y + dy < self.R):
            return board(self.R, self.C,
                         self.cells.union(placed))

    def __str__(self):
        rows = []
        rows.append('+'+'-'*self.C+'+')
        for y in range(self.R-1, -1, -1):
            row = ''
            for x in range(self.C):
                if (x, y) in self.cells:
                    row += 'O'
                else:
                    row += ' '
            rows.append('|'+row+'|')
        rows.append('+'+'-'*self.C+'+')
        return '\n'.join(rows)

def gen_mino_directions(mino):
    minos = []
    tmp = mino
    minos.append(tmp.cells)
    yield tmp
    for i in range(3):
        tmp = tmp.rotate()
        if tmp.cells not in minos:
            minos.append(tmp.cells)
            yield tmp
    tmp = mino.mirror()
    if tmp.cells not in minos:
        minos.append(tmp.cells)
        yield tmp
    for i in range(3):
        tmp = tmp.rotate()
        if tmp.cells not in minos:
            minos.append(tmp.cells)
            yield tmp

def search_rec(b, minos, R, C):
    """return if board can be filled with minos"""
    debug(b, 'R, C:', R, C)
    if not b:
        debug('board empty')
        return False
    if len(b.cells) == R*C:
        debug('solution found')
        return True
    for mino in minos:
        for m in gen_mino_directions(mino):
            for dx in range(C):
                for dy in range(R):
                    b_ = b.place_mino(m, dx, dy)
                    if search_rec(b_, minos, R, C):
                        return True
    return False

def solve_sub(b, Gabriel_mino, minos, R, C):
    """return if Gabriel can win with the mino `m`.
    in other words, solution exists for m"""
    for dx0 in range(C):
        for dy0 in range(R):
            for m in gen_mino_directions(Gabriel_mino):
                if search_rec(b.place_mino(m, dx0, dy0), minos, R, C):
                    return True

def solve(X, R, C):
    "return if RICHAD can win"
    minos = [m for m in gen_Xomino(X)]
    for m in minos:
        debug('trying:\n%s' % m),
        b = board(R, C)
        if not solve_sub(b, m, minos, R, C):
            debug('RICHARD wins with:\n%s' % m)
            return True
    debug('Gabriel wins with any mino')
    return False

def main():
    T = input()
    for i in range(T):
        X, R, C = map(int, raw_input().split(' '))
        if not check(X, R, C):
            print_result(i, 'RICHARD')
        else:
            if solve(X, R, C):
                print_result(i, 'RICHARD')
            else:
                print_result(i, 'GABRIEL')
                

if __name__ == '__main__':
    main()
