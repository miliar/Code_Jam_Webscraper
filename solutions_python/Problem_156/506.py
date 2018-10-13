inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %d"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")

T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    d, = parse_line()
    plates = parse_line()
    min_moves = max(plates)
    for i in xrange(2, 10):
        steps = 0
        for plate in plates:
            if plate > i:
                steps += plate/i - 1 + int(plate%i != 0)
        if min_moves > steps + i:
            min_moves = steps + i
    print >>outputfile, out_s % (ncase, min_moves)