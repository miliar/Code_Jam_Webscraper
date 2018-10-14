inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %d %d"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")

T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    N, = parse_line()
    plates = parse_line()
    
    eaten = 0
    last_plate = 0
    maxdiff = 0
    for ts, plate in enumerate(plates):
        if last_plate > plate:
            if last_plate - plate > maxdiff:
                maxdiff = last_plate - plate
            eaten += last_plate - plate
        last_plate = plate
    #print "maxdiff",maxdiff
    total = 0
    eaten2 = 0
    for plate in plates[:-1]:
        eaten2 += min(plate, maxdiff)

    print >>outputfile, out_s % (ncase, eaten, eaten2)