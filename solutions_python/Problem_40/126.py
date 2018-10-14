"""
Google Code Jam 2009
Round 1B
Challenge: A. Decision Tree

By Marcel Rodrigues

Code for Python 2.5+
"""

filename = "A-large"

inpath = filename + ".in"
outpath = filename + ".out"

infile = open(inpath, "r")
outfile = open(outpath, "w")

def cuteprobability(tree, features, p=1):
    p *= tree[0]
    if tree[1:]:
        identf = tree[1]
        if identf in features:
            return cuteprobability(tree[2], features, p)
        else:
            return cuteprobability(tree[3], features, p)
    else:
        return p

ncases = int(infile.readline().rstrip())

for case in range(ncases):
    outfile.write("Case #%d:\n" % (case + 1))
    nlines = int(infile.readline().rstrip())
    rawtree = " ".join([infile.readline().strip() for line in range(nlines)])
    rawtree = rawtree.replace("( ", "(")
    rawtree = rawtree.replace(" )", ")")
    rawtree = rawtree.replace("(", "[")
    rawtree = rawtree.replace(")", "]")
    rawtree = rawtree.replace(" ", ", ")
    cursor = 0
    rawlen = len(rawtree)
    objtree = ""
    while cursor < rawlen:
        char = rawtree[cursor]
        if char == ",":
            if rawtree[cursor + 2] != "[":
                objtree += ", '"
                cursor += 2
                identf = rawtree[cursor: rawtree.index(",", cursor)]
                objtree += identf + "'"
                cursor += len(identf)
                continue
        cursor += 1
        objtree += char
    objtree = eval(objtree)
    nanimals = int(infile.readline().rstrip())
    for animal in range(nanimals):
        line = infile.readline().rstrip()
        features = line.split(" ")[2:]
        p = cuteprobability(objtree, features)
        outfile.write("%.7f\n" % p)

infile.close()
outfile.close()
