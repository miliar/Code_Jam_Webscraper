inputfile = file("A-small.in", "rb")
outputfile = file("A-small.out", "wb")
out_s = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]

T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    first_row, = parse_line()
    rows_first_time = [parse_line() for i in xrange(4)]
    second_row, = parse_line()
    rows_second_time = [parse_line() for i in xrange(4)]
    possibles = set(rows_first_time[first_row-1]).intersection(set(rows_second_time[second_row-1]))
    if len(possibles) == 1:
        print >>outputfile, out_s % (ncase, list(possibles)[0])
    elif len(possibles) > 1:
        print >>outputfile, out_s % (ncase, "Bad magician!")
    elif len(possibles) == 0:
        print >>outputfile, out_s % (ncase, "Volunteer cheated!")
