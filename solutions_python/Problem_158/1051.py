f = open('input')
writing = open("output", "w")

n = 0
for i, line in enumerate(f):
    if (i == 0):
        n = int(line)
    else:
        x = 0
        r = 0
        c = 0
        parsed = line.strip().split()
        x = int(parsed[0])
        r = int(parsed[1])
        c = int(parsed[2])
        if (x == 1):
            writing.write("Case #" + str(i) + ": GABRIEL\n")
        elif (x == 2):
            if (((r % 2) == 0) or ((c % 2) == 0)):
                writing.write("Case #" + str(i) + ": GABRIEL\n")
            else:
                writing.write("Case #" + str(i) + ": RICHARD\n")
        elif (x == 3):
            if (((r % 3) == 0) or ((c % 3) == 0)):
                if ((r*c) == 3):
                    writing.write("Case #" + str(i) + ": RICHARD\n")
                else:
                    writing.write("Case #" + str(i) + ": GABRIEL\n")
            else:
                writing.write("Case #" + str(i) + ": RICHARD\n")
        else:
            if (((r == 3) and (c == 4)) or ((r == 4) and (c == 3))):
                writing.write("Case #" + str(i) + ": GABRIEL\n")
            elif ((r == 4) and (c == 4)):
                writing.write("Case #" + str(i) + ": GABRIEL\n")
            else:
                writing.write("Case #" + str(i) + ": RICHARD\n")
f.close()
writing.close()
