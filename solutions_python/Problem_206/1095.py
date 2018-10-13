def problem(inPath, outDir = ""):
    def solve(inPath, processor, outDir = ""):
        from multiprocessing import Pool
        from os import path

        inf = open(inPath, 'rU')
        stem = path.basename(inPath)
        name, extension = path.splitext(stem)
        outName = name + ".out"
        outPath = path.join(outDir, outName)
        outf = open(outPath, 'w')

        inf.readline() #discard the line which tells us how many lines of input there are
        pool = Pool()
        outputs = pool.map(processor, group(line.strip() for line in inf))
        for i, result in enumerate(outputs, 1):
            string = "Case #%s: %s" % (i, result)
            if i > 1:
                outf.write("\n")
            outf.write(string)

    solve(inPath, processor, outDir)

def group(lines):
    try:
        while True:
            d, n = map(int, next(lines).split())
            horses = []
            for i in range(n):
                ki, si = map(int, next(lines).split())
                horses.append((ki, si))
            yield (d, horses)
    except StopIteration:
        pass

def processor(args):
    d, horses = args
    return "{:f}".format(answer(d, horses))

def answer(d, horses):
    lastTime = 0
    for ki, si in horses:
        remaining = d - ki
        time = remaining/si
        lastTime = max(lastTime, time)

    return d/lastTime
