#!/usr/bin/python

import sys, os, math

 

def main():
    infile = open(sys.argv[1])
    outfile = open(os.path.splitext(sys.argv[1])[0]+".out", "w")
    
    cases = int(infile.readline())
    for case in range(cases):
        N, M = [int(x) for x in infile.readline().split()]
        existing = []
        wanted = []
        for i in range(N):
            existing.append(infile.readline().strip())
        existing.sort()
        for i in range(M):
            wanted.append(infile.readline().strip())
        wanted.sort()
        print "E", existing
        print "W", wanted
        mkdirs = 0
        for want in wanted:
            if want not in existing:
                # Find the longest existing prefix
                lprefix = ""
                for exist in existing:
                    prefix = os.path.commonprefix([exist.split("/"), want.split("/")])
                    if len(prefix) < len(lprefix):
                        break
                    lprefix = prefix
                print "W", want, "PRE", lprefix
                to_do = [x for x in want.split("/")[len(lprefix):] if x]
                print "TD", to_do
                print "MK", mkdirs, len(to_do)
                mkdirs += len(to_do)
                print "MK", mkdirs
                while want != "/" and want not in existing:
                    existing.append(want)
                    want = os.path.dirname(want)
                existing.sort()
                    
                print "E", "\n".join(existing)
        outfile.write("Case #%d: %d\n" % (case+1, mkdirs))

if __name__ == "__main__":
    main()