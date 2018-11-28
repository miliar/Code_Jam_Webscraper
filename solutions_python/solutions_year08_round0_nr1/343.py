def getSwitches(engines, words):
    w = 0
    maxw = 0
    switches = -1
    while w < len(words):
        for eng in engines:
            try:
                c = words.index(eng, w)
            except:
                c = len(words)
            if c > maxw:   
                maxw = c
        w = maxw
        switches += 1
    if switches == -1:
        switches = 0
    return switches


fname = "A-large.in"
fin = open(fname, "r")
fOutName = fname.split(".")[0] + ".out"
fout = open(fOutName, "w")
num = int(fin.readline().strip("\n"))
for i in xrange(1, num + 1):
    engines = []
    words = []
    numEngines = int(fin.readline().strip("\n"))
    for s in range(1, numEngines + 1):
        engines.append(fin.readline().strip("\n"))
    numWords = int(fin.readline().strip("\n"))
    for w in range(1, numWords + 1):
        words.append(fin.readline().strip("\n"))
    str = "Case #%d: %d" % (i, getSwitches(engines, words))
    print str
    fout.write(str + "\n") 
fin.close()
fout.close()
