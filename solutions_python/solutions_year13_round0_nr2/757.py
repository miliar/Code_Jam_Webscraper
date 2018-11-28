import time

debug = False

def checkreduceboard(board):

    while board:
        if debug:
            print '---'
            for row in board:
                print row
        nextpass = False
        boardmin = min(min(board[i]) for i in range(len(board)))
        for rc in range(len(board)):
            for cc in range(len(board[0])):
                if board[rc][cc] != boardmin:
                    continue
                else:
                    # found one. check horizontal
                    ok = True
                    for i in range(1,len(board[0])):
                        if board[rc][i] != board[rc][i-1]:
                            ok = False
                            break
                    if ok:
                        # remove current row
                        board = board[:rc] + board[rc+1:]
                    else:
                        for i in range(1,len(board)):
                            if board[i][cc] != board[i-1][cc]:
                                # This was the last chance!
                                return False
                        # it was ok, remove the column
                        for crow in range(len(board)):
                            board[crow] = board[crow][:cc] + board[crow][cc+1:]
                    # must have removed a row or a column to get here
                    nextpass = True
                    break
            if nextpass:
                break
    return True


tStart = time.time()

fname = "B-large"
#fname = "lawntest"

fin = open(fname+".in","r")
flines = fin.readlines()
fin.close()

fout = open(fname+".out","w")
numcases = int(flines[0])
curline = 1

for icase in range(1,numcases+1):
    answer = "YES"
    board = list()
    
    line = flines[curline].split()
    rows = int(line[0])
    cols = int(line[1])
    curline += 1

    badheight = False
    for r in range(rows):
        row = list()
        line = flines[curline].split()
        for c in range(cols):
            height = int(line[c])
            if height > 100:
                badheight = True
                break
            row.append(int(line[c]))
            if badheight:
                answer = "NO"
                break
        board.append(row)
        curline += 1

    if not badheight:
        if not checkreduceboard(board):
            answer = "NO"                                  

    outstr = "Case #%d: %s" % (icase,answer)
    print outstr
    fout.write("%s\n" % (outstr))
    
fout.close()

tEnd = time.time()

print "run time = %s" % (str((tEnd - tStart)))

dout = open("dummy.out","w")
row = ""
for c in range(100):
    row += " 1"
for r in range(100):
    dout.write("%s\n" % row)
dout.close()
    

            
