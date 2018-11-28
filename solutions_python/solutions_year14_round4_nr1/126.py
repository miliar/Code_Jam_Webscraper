infile = open("A-large.in", "rU")
outfile = open("A.out", "w")

ncases = int(infile.readline())

for case in xrange(1, ncases + 1):
    print case
    num_files, disc_capacity = [int(x) for x in infile.readline().strip().split(" ")]
    files = [int(x) for x in infile.readline().strip().split(" ")]

    files.sort()
    files.reverse()
    
    discs = []
    full_discs = 0
    for i in files:
        for j in xrange(len(discs)):
            if i + discs[j][0] <= disc_capacity:
                discs.pop(j)
                full_discs += 1

                break

        else:
            discs.append((i, 1))

    outfile.write("Case #%d: %d\n" % (case, len(discs) + full_discs))

infile.close()
outfile.close()
