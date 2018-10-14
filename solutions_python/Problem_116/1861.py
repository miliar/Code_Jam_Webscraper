f = open("A-large.in","r")

cases = int(f.readline().rstrip('\n'))

i = 0

while i < cases:

    i += 1

    row1 = f.readline().rstrip('\n')
    row2 = f.readline().rstrip('\n')
    row3 = f.readline().rstrip('\n')
    row4 = f.readline().rstrip('\n')

    column1 = row1[0]+row2[0]+row3[0]+row4[0]
    column2 = row1[1]+row2[1]+row3[1]+row4[1]
    column3 = row1[2]+row2[2]+row3[2]+row4[2]
    column4 = row1[3]+row2[3]+row3[3]+row4[3]

    diagonal1 = row1[0]+row2[1]+row3[2]+row4[3]
    diagonal2 = row1[3]+row2[2]+row3[1]+row4[0]
    
    f.readline()

    if row1[0:4] == "XXXX" or (row1.count("X")==3 and row1.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif row1[0:4] == "OOOO" or (row1.count("O")==3 and row1.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue  

    elif row2[0:4] == "XXXX" or (row2.count("X")==3 and row2.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif row2[0:4] == "OOOO" or (row2.count("O")==3 and row2.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue

    elif row3[0:4] == "XXXX" or (row3.count("X")==3 and row3.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif row3[0:4] == "OOOO" or (row3.count("O")==3 and row3.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue

    elif row4[0:4] == "XXXX" or (row4.count("X")==3 and row4.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif row4[0:4] == "OOOO" or (row4.count("O")==3 and row4.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue


    elif column1[0:4] == "XXXX" or (column1.count("X")==3 and column1.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif column1[0:4] == "OOOO" or (column1.count("O")==3 and column1.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue

    elif column2[0:4] == "XXXX" or (column2.count("X")==3 and column2.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif column2[0:4] == "OOOO" or (column2.count("O")==3 and column2.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue

    elif column3[0:4] == "XXXX" or (column3.count("X")==3 and column3.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif column3[0:4] == "OOOO" or (column3.count("O")==3 and column3.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue

    elif column4[0:4] == "XXXX" or (column4.count("X")==3 and column4.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif column4[0:4] == "OOOO" or (column4.count("O")==3 and column4.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue


    elif diagonal1[0:4] == "XXXX" or (diagonal1.count("X")==3 and diagonal1.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif diagonal1[0:4] == "OOOO" or (diagonal1.count("O")==3 and diagonal1.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue

    elif diagonal2[0:4] == "XXXX" or (diagonal2.count("X")==3 and diagonal2.count("T")==1):
        print "Case #" + str(i) + ": " + "X won"
        continue

    elif diagonal2[0:4] == "OOOO" or (diagonal2.count("O")==3 and diagonal2.count("T")==1):
        print "Case #" + str(i) + ": " + "O won"
        continue

    elif "." not in row1 and "." not in row2 and "." not in row3 and "." not in row4:
        print "Case #" + str(i) + ": " + "Draw"

    else:
        print "Case #" + str(i) + ": " + "Game has not completed"

















    



