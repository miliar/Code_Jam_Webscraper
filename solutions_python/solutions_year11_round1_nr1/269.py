#!/usr/bin/python

import sys

prec = .000001

def main():
    if len(sys.argv) < 3:
        print "Needs input and output files"
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')

    cases = int(fin.readline())

    for c in range(cases):
        possible = False
        s = fin.readline().strip().split(r' ')
        
        N = int(s[0])
        Pd = int(s[1]) / 100.0
        Pg = int(s[2]) / 100.0
        
        if Pg == 1 and Pd != 1:
            pass
        elif Pg == 0 and Pd != 0:
            pass
        else:
            for D in range(N + 1):
                if D == 0:
                    continue
                if abs(D * Pd - int(D * Pd)) < prec:
                    possible = True
                    print D
                    break
        
        fout.write("Case #%d: %s\n" % (c + 1, "Possible" if possible else "Broken")) 

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
