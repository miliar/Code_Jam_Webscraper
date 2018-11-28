dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def getAlt(pos):
    if pos[0] < 0 or pos[0] >= H:
        return 100000
    elif pos[1] < 0 or pos[1] >= W:
        return 100000
    else:
        return alts[pos[0]][pos[1]]

def getSink(pos):
    sink = pos
    sinkAlt = getAlt(pos)
    for dr in dirs:
        otherPos = (pos[0] + dr[0], pos[1] + dr[1])
        otherAlt = getAlt(otherPos)
        if (otherAlt < sinkAlt):
            sinkAlt = otherAlt
            sink = otherPos
    return sink

outFile = open("out.out", "w")
case = 1
inMap = False
for ind, line in enumerate(open("B-large.in","U")):
    if ind == 0:
        continue
    if not inMap:
        toks = line.split()
        H = int(toks[0])
        W = int(toks[1])
        curLine = 0
        alts = []
        sinks = {}
        inMap = True
        continue
    if (curLine < H):
        alts.append([])
        toks = line.split()
        for ind, tok in enumerate(toks):
            alts[curLine].append(int(tok))
        # print len(alts[curLine])
        curLine += 1
        if (curLine < H):
            continue
    # print alts
    # print "Done"
    outFile.write("Case #%d:\n" % case)
    for x in range(H):
        for y in range(W):
            pos = (x,y)
            sink = getSink(pos)
            if (sink == pos):
                sinks[pos] = pos
            else:
                sinks[pos] = sink
    for pos, sink in sinks.iteritems():
        while (True):
            newSink = sinks[sink]
            if newSink != sink:
                sink = newSink
            else:
                break
        sinks[pos] = sink
    name = "a"
    names = {}
    for x in range(H):
        line = ""
        for y in range(W):
            pos = (x,y)
            sink = sinks[pos]
            cn = names.get(sink)
            if cn is None:
                cn = name
                names[sink] = cn
                name = chr(ord(name)+1)
            line += cn
            if y != W-1:
                line += " "
            else:
                # print line
                line += "\n"
        outFile.write(line)
    inMap = False
    case += 1
outFile.close()
