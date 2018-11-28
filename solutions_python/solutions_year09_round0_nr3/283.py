"""
Google Code Jam 2009
Challenge: C. Welcome to Code Jam

By Marcel Rodrigues

Code for Python 2.5+
"""

inpath = "C-small-attempt1.in"
outpath = "C-small-attempt1.out"

def treecount(text, phrase, pindex=0):
    if pindex == len(phrase):
        return 1
    char = phrase[pindex]
    freq = text.count(char)
    if not freq:
        return 0
    s = 0
    for f in range(freq):
        i = text.index(char)
        text = text[i + 1:]
        s += treecount(text, phrase, pindex + 1)
        s = s % 10000
    return s

phrase = "welcome to code jam"

infile = open(inpath, "r")
outfile = open(outpath, "w")

N = int(infile.readline().rstrip())

for n in range(N):
    text = infile.readline().rstrip()
    outfile.write("Case #%d: %s\n" % (n + 1, str(treecount(text, phrase)).rjust(4, "0")))

infile.close()
outfile.close()