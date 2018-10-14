f = open('A-large.in', 'r')
T = int(f.readline().strip())

for t in xrange(T):
    l = []
    lT=[]
    won = False
    winners = ""
    for i in range(4):
        l.append(f.readline().strip())
    l += map(list, zip(*l))
    l.append(''.join([l[x][x] for x in range(4)]))
    l.append(''.join([l[3-x][x] for x in range(4)]))
    linesFull = 0

    for line in l+lT:
        if line.count("O") == 4 or (line.count("O") == 3 and line.count("T") == 1):
            winners += "O"
        if line.count("X") == 4 or (line.count("X") == 3 and line.count("T") == 1):
            winners += "X"
        if line.count(".") == 0:
            linesFull += 1

    if winners.count("X") > 0:
        if winners.count("O") > 0:
            res = "Draw"
        else:
            res = "X won"
    elif winners.count("O") > 0:
        res = "O won"
    else:
        if linesFull == 10:
            res = "Draw"
        else:
            res = "Game has not completed"
            
    s = "Case #%d: %s\n" % (t+1, res)
    with open("delta.out", "a") as o:
        o.write(s)
    f.readline()
