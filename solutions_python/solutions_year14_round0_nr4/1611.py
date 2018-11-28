infile = open("D-large.in", "rU")
outfile = open("D_small.out", "w")

ncases = int(infile.readline())

for case in xrange(1, ncases + 1):
    nblocks = int(infile.readline())

    naomi_w = [float(x) for x in infile.readline().strip().split(" ")]
    ken_w = [float(x) for x in infile.readline().strip().split(" ")]

    naomi_w.sort()
    ken_w.sort()

    naomi_d = naomi_w[:]
    ken_d = ken_w[:]
    
    war = 0
    deceitful = 0

    # Play War
    while len(naomi_w) > 0:
        block = naomi_w.pop(0)

        # Should binary search here for large input

        for i in ken_w:
            if i > block:
                ken_w.remove(i)
                break

        else:
            ken_w.pop(0)
            war += 1

    # Play Deceitful War
    while len(ken_d) > 0:
        block = ken_d.pop(0)

        # Should binary search here for large input

        for i in naomi_d:
            if i > block:
                naomi_d.remove(i)
                deceitful += 1                
                break

        else:
            naomi_d.pop(0)
    

    outfile.write("Case #%d: %d %d\n" % (case, deceitful, war))

outfile.close()
