#!/usr/bin/env python
import sys

def process(length, horses):
    print length, horses
    m = None
    for horse in horses:
        dt = (length - horse[0]) / float(horse[1])
        mh = length / dt
        if m is None:
            m = mh
            continue
        if mh < m:
            m = mh
    
    return m

with open(sys.argv[2], "w") as fout:
    with open(sys.argv[1]) as fin:
        c = -1
        horses = list()
        hs = 0
        for line in fin:
            if c == -1:
                c += 1
                continue
            ln = line[:-1].split(" ")
            if hs == 0:
                if len(horses) > 0:
                    n = process(length, horses)
                    c += 1
                    fout.write("Case #{}: ".format(c) + "{0:f}".format(n) + "\n")
                    horses = list()
                    hs = 0
                length = long(ln[0])
                hs = int(ln[1])
            else:
                horses.append([long(l) for l in ln])
                hs -= 1
        n = process(length, horses)
        c += 1
        fout.write("Case #{}: ".format(c) + str(n) + "\n")
        
            # if lines == 0:
            #     n = process(horses)
            #     if n == -1:
            #         fout.write("Case #{}: IMPOSSIBLE\n".format(c))
            #     else:
            #         fout.write("Case #{}: ".format(c) + str(n) + "\n")
            # else:
            #     horses.append(line[:-1])
            # lines -= 1
                
