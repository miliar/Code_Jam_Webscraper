def main(filein):
    f = open(filein, "r")
    outname = filein.split(".")[0] + "OUT.txt"
    g = open(outname, "w")

    count = 0 # account for silly first line
    temp = 0
    init = ""
    for line in f:
        if count == 0:
            count += 1
            continue
        if temp < 4:
            if line[-1] == "\n":
                line = line[:-1]
            init += line
            temp += 1
        else:
            print ""
            newline = "Case #" + str(count) + ": " + code(init) + "\n"
            g.write(newline)
            temp = 0
            count += 1
            init = ""
    
    count = -1
    for line in f:
        count += 1
        if count == 0:
            continue
        newline = "Case #" + str(count) + ": " + code(line) + "\n"
        g.write(newline)
    
    f.close()
    g.close()
    
def code(line):
    # vals are four rows, then four cols, then two diagonals
    # multiply by 2 for X, 3 for O - then 8,16 mean x win and 27,81 mean y win
    vals = [1,1,1,1,1,1,1,1,1,1]
    isDone = True
    for (i, char) in enumerate(line):
        row = i / 4 # 0123, 4567, 891011, 12131415
        col = 4 + (i % 4) # 04812 ...
        if char == "T":
            continue
        elif char == ".":
            isDone = False
            continue
        elif char == "X":
            mult = 2
        else: # char == "O"
            mult = 3            
        vals[row] *= mult
        vals[col] *= mult
        if i in [0,5,10,15]:
            vals[8] *= mult
        elif i in [3,6,9,12]:
            vals[9] *= mult
    for v in vals:
        if v == 8 or v == 16:
            return "X won"
        elif v == 27 or v == 81:
            return "O won"
    if not isDone:
        return "Game has not completed"
    else:
        return "Draw"