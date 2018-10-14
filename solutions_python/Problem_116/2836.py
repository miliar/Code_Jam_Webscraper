import os

infilename = "A-small-attempt2.in"
in_file = open(infilename)

numcases = int(in_file.readline())
totalout = ""

for casenum in range(numcases):
    game_grid = dict()
    for i in range(4):
        line = in_file.readline()
        for j in range(4):
            game_grid[(i, j)] = line[j]
    in_file.readline()
    
    for i in range(4):
        winner = True
        firstsym = game_grid[(i, 0)]
        if firstsym == "T":
            firstsym = game_grid[(i, 1)]
        if firstsym == ".":
            winner = False
        for j in range(1, 4):
            if game_grid[(i, j)] == 'X':
                if firstsym == 'O':
                    winner = False
                    break
            elif game_grid[(i, j)] == 'O':
                if firstsym == 'X':
                    winner = False
                    break
            elif game_grid[(i, j)] == '.':
                winner = False
                break
            elif game_grid[(i, j)] == 'T':
                pass
        if winner:
            break

    if not winner:
        for i in range(4):
            firstsym = game_grid[(0, i)]
            if firstsym == "T":
                firstsym = game_grid[(1, i)]
            winner = True
            if firstsym == ".":
                winner = False
            for j in range(1, 4):
                if game_grid[(j, i)] == 'X':
                    if firstsym == 'O':
                        winner = False
                        break
                elif game_grid[(j, i)] == 'O':
                    if firstsym == 'X':
                        winner = False
                        break
                elif game_grid[(j, i)] == '.':
                    winner = False
                    break
                elif game_grid[(j, i)] == 'T':
                    pass
            if winner:
                break

    if not winner:
        winner = True
        firstsym = game_grid[(0, 0)]
        if firstsym == "T":
            firstsym = game_grid[(1, 1)]
        if firstsym == ".":
            winner = False
        for i in range(1, 4):
            if game_grid[(i, i)] == 'X':
                if firstsym == 'O':
                    winner = False
                    break
            elif game_grid[(i, i)] == 'O':
                if firstsym == 'X':
                    winner = False
                    break
            elif game_grid[(i, i)] == '.':
                winner = False
                break
            elif game_grid[(i, i)] == 'T':
                pass

    if not winner:
        winner = True
        firstsym = game_grid[(0, 3)]
        if firstsym == "T":
            firstsym = game_grid[(1, 2)]
        if firstsym == ".":
            winner = False
        for i in range(1, 4):
            if game_grid[(i, 3-i)] == 'X':
                if firstsym == 'O':
                    winner = False
                    break
            elif game_grid[(i, 3-i)] == 'O':
                if firstsym == 'X':
                    winner = False
                    break
            elif game_grid[(i, 3-i)] == '.':
                winner = False
                break
            elif game_grid[(i, 3-i)] == 'T':
                pass

    if not winner:
        completed = True
        for i in range(4):
            for j in range(4):
                if game_grid[(i, 1)] == '.':
                    completed = False

    if winner:
        outstr = "Case #" + str(casenum + 1) + ": " + firstsym + " won"
    else:
        if completed:
            outstr = "Case #" + str(casenum + 1) + ": " + "Draw"
        else:
            outstr = "Case #" + str(casenum + 1) + ": " + "Game has not completed"

        
    totalout += outstr + "\n"
    print(outstr)


writetofile = True
if "small" in infilename:
    outprefix = "small"
    writetofile = True
elif "large" in infilename:
    outprefix = "large"
    writetofile = True
#writetofile = False

if writetofile:
    filenum = 0
    while True:
        outfilename = outprefix + str(filenum) + ".out"
        filenum += 1
        if not os.path.isfile(outfilename):
            break
    out_file = open(outfilename, 'w+')
    out_file.write(totalout)
    out_file.close()

in_file.close()

