import sys

def read_arrangement(f):
    arr = [ f.readline(), f.readline(), f.readline(), f.readline() ]
    arr = [ line.strip().split() for line in arr ]
    return arr

def read_possible_values(f):
    row = int(f.readline())
    arr = read_arrangement(f)
    cards = set([ int (x) for x in arr[row - 1] ])
    return cards

with open(sys.argv[1]) as f:
    T = int(f.readline())

    for case in xrange(T):
        row1 = read_possible_values(f)
        row2 = read_possible_values(f)
        cards = row1 & row2
        
        print "Case #%d:" % (case + 1),
        if len(cards) < 1:
            print "Volunteer cheated!"
        if len(cards) > 1:
            print "Bad magician!"
        else:
            for x in cards:
                print x


        
