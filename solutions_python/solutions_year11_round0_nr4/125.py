outfile = open("outputLarge.txt", "w")

linenum = 0
case = 1
for line in open("D-large.in", "rU"):
    if linenum > 0 and linenum % 2 == 0:
        listy = line.split(" ")
        intlisty = []
        anslisty = []
        number = 1 
        for item in listy:
            intlisty.append(int(item))
            anslisty.append(number)
            number += 1
        n = 0
        for index in xrange(0, len(intlisty)):
            if intlisty[index] != anslisty[index]:
                n += 1
        outfile.write("Case #" + str(case) + ": " + str(n) + ".000000\n")
        case += 1
    linenum += 1

outfile.close
