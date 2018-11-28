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
        outputs = pool.map(processor, (line.strip() for line in inf))
        for i, result in enumerate(outputs, 1):
            string = "Case #%s: %s" % (i, result)
            if i > 1:
                outf.write("\n")
            outf.write(string)

    solve(inPath, processor, outDir)

def processor(string):
    split = string.split(" ")
    faces = [f == "+" for f in split[0]]
    k = int(split[1])
    result = answer(faces, k)
    if result is None:
        return "IMPOSSIBLE"
    return result

def prettyprint(faces):
    return "".join("+" if f else "-" for f in faces)

def answer(faces, k):
    def flip(index):
##        print("BEFORE:", prettyprint(faces))
        for i in range(index, index + k):
            faces[i] = not faces[i]
##        print("AFTER:", prettyprint(faces))
    
    if k > len(faces):
        return None

    flips = 0
    for index in range(len(faces) + 1 - k):
        if not faces[index]:
            flips += 1
            flip(index)
    if all(faces):
        return flips
    return None
