import sys

class Grid:
    def __init__(self, input_file):
        self.selected = int(next(input_file).strip()) - 1
        self.rows = []
        all = set()
        for r in range(4):
            row = next(input_file).strip().split( )
            self.rows.append(set(row))
            all = all.union(self.rows[r])
        if len(all) != 16:
            raise RuntimeError("Expected 16 unique numbers - %s" % all)

if len(sys.argv) != 2:
    raise RuntimeError("usage: %s inputFile" % sys.argv[0])

with open(sys.argv[1], 'r') as input:
    tests = next(input).strip()
    for i in range(1, int(tests)+1):
        first = Grid(input)
        second = Grid(input)
        results = first.rows[first.selected].intersection(second.rows[second.selected])
        if len(results) == 1:
            result = results.pop()
        elif len(results) > 1:
            result = "Bad magician!"
        else:
            result = "Volunteer cheated!"
        print "Case #%d: %s" % (i, result)

