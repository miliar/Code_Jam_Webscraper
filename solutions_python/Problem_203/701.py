infile = open("A-large.in", "r")
outfile = open("Aout.txt", "w")

tcase = int(infile.readline().rstrip())
for z in range(1, tcase+1):
    inline = infile.readline().rstrip()
    row, col = inline.split()
    row = int(row)
    col = int(col)
    cake = []
    for i in range(0, row):
        cake.append(list(infile.readline().rstrip()))
    for i in range(0, row):
        emptyrow = False
        for j in range(1, col):
            #try and pull the one behind
            if cake[i][j] == "?":
                cake[i][j] = cake[i][j-1]
        #try and pull forward
        for j in range(col-2, -1, -1):
            if cake[i][j] == "?":
                cake[i][j] = cake[i][j+1]
        for j in range(0, col):
            if cake[i][j] == "?":
                emptyrow = True
        if emptyrow == True and i > 0:
            for j in range(0, col):
                cake[i][j] = cake[i-1][j]
    #check if need to pull up
    for i in range(row-2, -1, -1):
        emptyrow = False
        for j in range(0, col):
            if cake[i][j] == "?":
                emptyrow = True
        if emptyrow == True:
            for j in range(0, col):
                cake[i][j] = cake[i+1][j]
    #print(cake)
    outline = "Case #" + str(z) + ":\n"
    outfile.write(outline)
    for i in range(0, row):
        outline = ""
        for j in range(0, col):
            outline += cake[i][j]
        outfile.write(outline + "\n")
        #print(outline)
outfile.close()
