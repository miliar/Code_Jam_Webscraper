#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for i in range(ncases) :
        line = f.readline().split()

        C = int(line[0])
        cs = line[1:1+C]

        D = int(line[1+C])
        ds = line[2+C:2+C+D]

        N = int(line[2+C+D])
        string = line[3+C+D]

        out = ''
        for k in xrange(N) :
            if len(out) == 0:
                out = string[k]
            else :
            
                end = out[-1] + string[k]

                replaced = False
                for c in cs :
                    if (end == c[0:2]) or (end == c[1::-1]) :
                        out = out[:-1] + c[2]
                        replaced = True
                        break
                if not replaced :
                    for d in ds :
                        if (string[k] == d[0]) and (d[1] in out) :
                            out = ''
                        elif (string[k] == d[1]) and (d[0] in out) :
                            out = ''
                        else :
                            out += string[k]

                    if len(ds) == 0 :
                        out += string[k]
                            
        print 'Case #%i:'%(i+1), 
        print str(list(out)).replace("'", "")
    
    f.close()

main()
