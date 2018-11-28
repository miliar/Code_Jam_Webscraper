f = open("b.in", "rU")
def special(numPancakes, splits):
    piece = numPancakes//(splits+1)
    if numPancakes-piece*(splits+1) > 0:
        piece += 1 #Round piece size up
    return (numPancakes, splits, piece)
        
def ri():#int
    return int(f.readline().strip())
def rl(sep=False):#list of string
    if not sep:
        return f.readline().split()
    return f.readline().split(sep)

cases = ri()####
out = ""####
for case in range(cases):####
    d = ri()
    # (originalSize, numSplits, pieceSize)
    p = [(int(i), 0, int(i)) for i in rl()]
    p.sort(lambda stack: stack[2])
    splits = 0
    minutes = 0
    biggest = p[d-1][2]
    originalBiggest = biggest
    bestMinutes = biggest
    while splits < originalBiggest and biggest > 3:
        p[d-1] = special(p[d-1][0], p[d-1][1]+1)
        splits += 1
        p.sort(lambda stack: stack[2])
        biggest = p[d-1][2]
        minutes = splits + biggest
        if minutes < bestMinutes:
            bestMinutes = minutes
    out += "Case #{}: {}\n".format(case+1, bestMinutes)####
f.close()####
out = out.strip()####
o = open("b.out", "w")####
o.write(out)####
o.close()####