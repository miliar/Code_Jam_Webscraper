inp = "B-large.in"
txt = open(inp).readlines()
txt = [x.strip() for x in txt]

entries = int(txt.pop(0))

def pad(x):
    if len(x) == 1:
        return "0" + x
    return x

def addtime(time, turn):
    time = time.split(":")
    time = [int(x) for x in time]
    time[1] += turn
    if time[1] > 59:
        time[0] += time[1] / 60
        time[1] = time[1] % 60
    time = [pad(str(x)) for x in time]
    return ":".join(time)

cases = []
for i in xrange(entries):
    tround = int(txt.pop(0))
    l, r = txt.pop(0).split()
    left = txt[:int(l)]
    txt = txt[int(l):]
    right = txt[:int(r)]
    txt = txt[int(r):]

    left = [x.split() for x in left]
    right = [x.split() for x in right]

    cases.append( ( tround, left, right ) )

f = open('.'.join([inp.split(".")[0], "out"]), "w")
for casenum, ( tround, left, right ) in enumerate(cases):
    #Trains used
    lused = 0
    rused = 0
    
    #Trains spare at these times    
    larr = sorted([addtime(x[1], tround) for x in right])
    rarr = sorted([addtime(x[1], tround) for x in left])

    #Trains departing at these times
    ldep = sorted([x[0] for x in left])
    rdep = sorted([x[0] for x in right])

    #print ldep

    for t in ldep:
        if larr and min(larr) <= t:
            larr.remove(min(larr))
        else:
            lused += 1

    for t in rdep:
        if rarr and min(rarr) <= t:
            rarr.remove(min(rarr))
        else:
            rused += 1

    print "="*5
    print tround
    print left
    print right
    print
    print "Case #%d: %d %d\n" % (casenum+1, lused, rused)
    f.write( "Case #%d: %d %d\n" % (casenum+1, lused, rused) )
f.close()
print "Done"
