outfile = open("outputB.txt", "w")
linenum = 0
case = 1
for line in open("B-small-attempt1.in","rU"):
    if linenum != 0:
        listy = line.strip().split(" ")
        boosters = int(listy[0])
        buildtime = int(listy[1])
        distances = int(listy[2])
        starlist = []
        n = 4
        while len(starlist) < distances:
            starlist.append(int(listy[n]))
            n += 1
            if n >= len(listy):
                n = 4
        travelled = 0
        total = sum(starlist)*2
        while travelled < float(buildtime):
            travelled += 2
            starlist[0] -= 1
            if starlist[0] <= 0:
                starlist.remove(starlist[0])
                if len(starlist) == 0:
                    break
        #print starlist
        starlist.sort()
        starlist.reverse()
        total -= sum(starlist[:(boosters)])
        outfile.write("Case #" + str(case) + ": " + str(int(total)) + "\n")
        case += 1
    linenum += 1
outfile.close()
