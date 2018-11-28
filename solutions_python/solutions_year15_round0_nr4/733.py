infile = open("D-small-attempt0.in", "r")
outfile = open("outputD.txt", "a")

lines = infile.readlines()

count = 0
g = True

for line in lines:
    count += 1
    if count == 1:
        pass
    else:
        line = line[:-1].split()
        if line[0] == "1":
            g = True
        elif line[0] == "2":
            if (int(line[1]) * int(line[2])) % 2 == 1:
                g = False
            else:
                g = True
        elif line[0] == "3":
            if (int(line[1]) * int(line[2])) % 3 == 0 and int(line[1]) != 1 and int(line[2]) != 1:
                g = True
            else:
                g = False
        elif line[0] == "4":
            if (int(line[1]) * int(line[2])) % 4 == 0 and int(line[1]) > 2 and int(line[2]) > 2:
                g = True
            else:
                g = False

        if g == True:
            outfile.write("Case #" + str(count-1) + ": GABRIEL\n")
        else:
            outfile.write("Case #" + str(count-1) + ": RICHARD\n")

outfile.close()
infile.close()
