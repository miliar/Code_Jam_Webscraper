import sys

filename = sys.argv[1]
print "Using file", filename
inputf = open(filename, 'r')
outputname = filename[:-2] + "out"
outputf = open(outputname, 'w')

def perm(l):
    sz = len(l)
    if sz <= 1:
        return [l]
    return [p[:i]+[l[0]]+p[i:] for i in xrange(sz) for p in perm(l[1:])]

cases = int(inputf.readline())
print cases, "test cases"
for case in range(1, cases + 1):
    outputf.write("Case #" + str(case) + ": ")
    print "Case", case
    
    cells, reln = tuple( int(v) for v in inputf.readline()[:-1].split() )    
    releases = tuple( int(v) for v in inputf.readline()[:-1].split() )
    
    print cells, reln, releases
    
    minn = None
    for p in perm(list(releases)):
        curr = list(range(1, cells + 1))
        bb = 0
        for c in p:
            curr.remove(c)
            nextc = c + 1
            while nextc in curr:
                nextc += 1
            numr = nextc - 1 - c
            prevc = c - 1
            while prevc in curr:
                prevc -= 1
            numl = c - (prevc + 1)
            bb = bb + numr + numl
        if minn == None or bb < minn:
            minn = bb
    
    print minn
    outputf.write(str(minn) + "\n")
            
    
inputf.close()
outputf.close()
