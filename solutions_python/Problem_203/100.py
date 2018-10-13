import sys
stdin = sys.stdin
ncases = int(stdin.readline())

class Range2D:
    def __init__(self, t, l, b, r):
        self.t = t
        self.l = l
        self.b = b
        self.r = r
    
    @staticmethod
    def fromPos(pos):
        return Range2D(pos[0], pos[1], pos[0] + 1, pos[1] + 1)
    
    def combine(self, o):
        return Range2D(min(self.t, o.t), min(self.l, o.l), max(self.b, o.b), max(self.r, o.r))
    
    def vRange(self):
        return range(self.t, self.b)

    def hRange(self):
        return range(self.l, self.r)

class Letter:
    def __init__(self, letter, range):
        self.letter = letter
        self.range = range
    
    def combine(self, o):
        return Letter(self.letter, self.range.combine(o))
    
    def __repr__(self):
        return "Letter<{0}, {1}-{2} {3}-{4}>".format(self.letter, self.range.t, self.range.b, self.range.l, self.range.r)

class Soln:
    def __init__(self, grid, letters):
        self.grid = grid
        self.letters = letters

    @staticmethod
    def fromGrid(grid):
        letters = {}
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != '?':
                    if val in letters:
                        letters[val].combine(Range2D.fromPos((r, c)))
                    else:
                        letters[val] = Letter(val, Range2D.fromPos((r, c)))
        return Soln(grid, letters)

    def clone(self):
        grid = [[v for v in row] for row in self.grid]
        letters = dict((l, v) for l, v in self.letters.items())
        return Soln(grid, letters)

    def printGrid(self):
        return '\n'.join(''.join(row) for row in self.grid)

for ncase in range(ncases):
    R, C = map(int, stdin.readline().strip().split(' '))
    grid = []
    for i in range(R):
        grid.append([x for x in stdin.readline().strip()])


    def next(a):
        r = a[0]
        c = a[1]
        c += 1
        if c == C: r += 1; c = 0
        if r == R: return None
        return (r, c)

    def find_soln(g, pos):
        if pos == None: return g
        if g.grid[pos[0]][pos[1]] != '?': return find_soln(g, next(pos))
        for letter in g.letters.values():
            g2 = tryExpand(g, pos, letter)
            if g2 is not None:
                soln = find_soln(g2, next(pos))
                if soln is not None:
                    return soln

    def tryExpand(g, pos, letter):
        l = letter.combine(Range2D.fromPos(pos))
        for r in l.range.vRange():
            for c in l.range.hRange():
                if g.grid[r][c] != '?' and g.grid[r][c] != l.letter:
                    return None
        
        g = g.clone()
        for r in l.range.vRange():
            for c in l.range.hRange():
                g.grid[r][c] = l.letter
        g.letters[l.letter] = l
        # print("trying {0} at {1} ({3}) in\n{2}".format(l.letter, pos, g.printGrid(), l))
        return g


    initial = Soln.fromGrid(grid)
    # print(initial.letters, initial.printGrid())
    final = find_soln(initial, (0, 0))

    print('Case #{0}:\n{1}'.format(ncase + 1, final.printGrid()))