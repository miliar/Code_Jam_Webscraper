infile = open("A-small-attempt0.in", "rU")
outfile = open("A_small.out", "w")

t = int(infile.readline())

linenum = 0
case = 1

for case in xrange(1, t+1):
    first_num = int(infile.readline())
    possibilities = []

    for i in xrange(1, 4+1):
        line = [int(x) for x in infile.readline().split(" ")]

        if i == first_num:
            possibilities.extend(line)

    second_num = int(infile.readline())

    for i in xrange(1, 4+1):
        line = [int(x) for x in infile.readline().split(" ")]

        if i == second_num:
            found = []

            for x in possibilities:
                for y in line:
                    if x == y:
                        found.append(x)

            if len(found) == 0:
                outfile.write("Case #%d: Volunteer cheated!\n" % case)

            elif len(found) == 1:
                outfile.write("Case #%d: %d\n" % (case, found[0]))

            else:
                outfile.write("Case #%d: Bad magician!\n" % case)

outfile.close()
                


