# Ominous Omino

try:
    output = open('OminousOminoOutput.txt', 'w')
    
    file = open('D-small-attempt4.in', 'r')
    file = file.readlines()
    testcases = int(file[0].rstrip())
    for i in range(1, testcases+1):
        line = file[i].split()
        x = int(line[0])
        r = int(line[1])
        c = int(line[2])

        if x == 1:
            output.write("Case #%d: GABRIEL\n" % (i))
        elif x == 2:
            if (r == 1 and c == 2) or (r == 2 and c == 1):
                output.write("Case #%d: GABRIEL\n" % (i))
            elif (r == 1 and c == 4) or (r == 4 and c == 1):
                output.write("Case #%d: GABRIEL\n" % (i))
            elif (r == 3 and c == 4) or (r == 4 and c == 3):
                output.write("Case #%d: GABRIEL\n" % (i))
            elif (r == 2 and c == 3) or (r == 3 and c == 2):
                output.write("Case #%d: GABRIEL\n" % (i))
##            elif (r == 1 and c == 3) or (r == 3 and c == 1):
##                output.write("Case #%d: RICHARD\n" % (i))
            elif (r%2 != 0) or (c%2 != 0):    # odd
                output.write("Case #%d: RICHARD\n" % (i))
            else:   # even
                output.write("Case #%d: GABRIEL\n" % (i))
        elif x == 3:
            if (r <= 2) and (c <= 2):
                output.write("Case #%d: RICHARD\n" % (i))
            elif (r == 1 and c == 3) or (r == 3 and c == 1):
                output.write("Case #%d: RICHARD\n" % (i))
            elif (r == 1 and c == 4) or (r == 4 and c == 1):
                output.write("Case #%d: RICHARD\n" % (i))
            elif (r == 4 and c == 2) or (r == 2 and c == 4):
                output.write("Case #%d: RICHARD\n" % (i))
            elif (r == 4 and c == 4) or (r == 4 and c == 4):
                output.write("Case #%d: RICHARD\n" % (i))
            else:
                output.write("Case #%d: GABRIEL\n" % (i))
            
        else: # x == 4
            if (r == 4) and (c == 4):
                output.write("Case #%d: GABRIEL\n" % (i))
            elif (r == 3 and c == 4) or (r == 4 and c == 3):
                output.write("Case #%d: GABRIEL\n" % (i))
            else:
                output.write("Case #%d: RICHARD\n" % (i))

    output.close()

except FileNotFoundError:
    print("File Not Found!")
