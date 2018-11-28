import csv
import sys


def read_table(infile):
    row = int(infile.next()[0])
    rows = [infile.next() for x in range(4)]
    return set(map(int, rows[row - 1]))


infile = csv.reader(open(sys.argv[1], 'r'), delimiter=' ')

cases = int(infile.next()[0])

for case in xrange(cases):
    first_row = read_table(infile)
    second_row = read_table(infile)
    
    cards = first_row & second_row
    count = len(cards)
    
    if count == 0:
        result = "Volunteer cheated!"
    elif count == 1:
        result = str(list(cards)[0])
    else:
        result = "Bad magician!"

    print "Case #%u: %s" % (case + 1, result)
    