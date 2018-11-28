#!/usr/bin/env python

import sys

out = []

with open(sys.argv[1],'r') as f:
    t = int(f.readline())

    for z in range(t):
        done=False
        lines = []
        for i in range(4):
            lines.append(f.readline().strip())
        f.readline()
        for xo in ["X","O"]:
            xot = [xo,"T"]
            for i in range(4):
                if lines[i][0] in xot and lines[i][1] in xot and lines[i][2] in xot and lines[i][3] in xot:
                    out += [xo+" won"]
                    done=True
                    break
                elif lines[0][i] in xot and lines[1][i] in xot and lines[2][i] in xot and lines[3][i] in xot:
                    out += [xo+" won"]
                    done=True
                    break
            if done:
                break
            if lines[0][0] in xot and lines[1][1] in xot and lines[2][2] in xot and lines[3][3] in xot:
                out += [xo+" won"]
                done=True
                break
            elif lines[3][0] in xot and lines[2][1] in xot and lines[1][2] in xot and lines[0][3] in xot:
                out += [xo+" won"]
                done=True
                break
        if done:
            continue
        for i in range(4):
            if '.' in lines[i]:
                out += ["Game has not completed"]
                done=True
                break
        if done:
            continue
        out += ["Draw"]

for x in range(len(out)):
    print "Case #%d: %s"%(x+1,out[x])
