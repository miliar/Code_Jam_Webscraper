def Move(opos, bpos, seq):
    nseq = seq[:]
    # Run the behaviour of O
    if seq[0][0] == "O" and seq[0][1] == opos:
        nseq = seq[1:]
    else:
        n = 0
        while seq[n][0] != "O" and n < len(seq) - 1:
            n += 1
        if seq[n][1] > opos:
            opos += 1
        elif seq[n][1] < opos:
            opos -= 1
    # Run the behaviour of B
    if seq[0][0] == "B" and seq[0][1] == bpos:
        nseq = seq[1:]
    else:
        n = 0
        while seq[n][0] != "B" and n < len(seq) - 1:
            n += 1
        if seq[n][1] > bpos:
            bpos += 1
        elif seq[n][1] < bpos:
            bpos -= 1
    return (opos, bpos, nseq)

def Sim(sequence):
    se = sequence[:]
    op = 1
    bp = 1
    t = 0
    while len(se) > 0:
        t += 1
        mov = Move(op, bp, se)
        op = mov[0]
        bp = mov[1]
        se = mov[2]
    return t

fin = file("bot.in")
lines = fin.readlines()
count = int(lines[0])
for i in range(1, count + 1):
    s = []
    ls = lines[i].split(" ")
    for j in range(0, int(ls[0])):
        s += [[ls[2 * j + 1], int(ls[2 * j + 2])]]
    print "Case #" + str(i) + ": " + str(Sim(s))
