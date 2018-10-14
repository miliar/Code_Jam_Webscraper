def dotestcase(casenr, inp, out):
    S = int(inp.readline())
    engines = {}
    for i in range(S):
        engines[inp.readline()] = i
    sws = [0] * S;
    for i in range(int(inp.readline())):
        query = inp.readline()
        searchedengine = engines[query];
        if searchedengine!=None:
            minim = min(sws) + 1
            sws[searchedengine] += 1
            sws[searchedengine] = min(sws)+1
            for i in range(S):
                if i!=searchedengine:
                    sws[i] = min(sws[i], minim)
    out.write("Case #%d: %d\n" % (casenr, min(sws)))

import sys
#f = sys.stdin
f=open("input.txt")
g = open("output.txt", "w")

N = int(f.readline())

for i in range(N):
    dotestcase(i+1, f, g)
g.close()
