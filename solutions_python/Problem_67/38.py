# Cartesian product generator
import itertools

# Conway, but "sparse". Infinite grid, finite number of cells.
def simulation(cells):
    # Store all as sets.
    birthr, birthd, newcells = set(), set(), set()

    # For each cell:
    for x,y in set(cells):
        # Mark its bottom and right neighbour as "potential" birth.
        birthr.add((x+1,y))
        birthd.add((x,y+1))

    # All cells seeded both from the left and the top are born:
    for x,y in birthr.intersection(birthd):
        newcells.add((x,y))
    # All cells already alive stay alive if they are in one of the two:
    for x,y in set(cells).intersection(birthd.union(birthr)):
        newcells.add((x,y))
    return newcells

def exterminate(cells):
    turns = 0
    while len(cells):
        cells = simulation(cells)
        turns += 1
    return turns


def main():
    cases = int(raw_input())
    for case in xrange(cases):
        blocks = int(raw_input())
        cells = []
        for block in xrange(blocks):
            x1,y1,x2,y2 = map(int, raw_input().split(" "))
            cells += itertools.product(range(x1,x2+1),range(y1,y2+1))
        print "Case #%d: %d" % (case + 1, exterminate(set(cells)))

            
        
main()
