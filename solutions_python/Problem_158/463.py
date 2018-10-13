#!/usr/bin/env python
import sys

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

def ew(s):
    ferr.write("%s\n" % s)

def ew0(s):
    pass

def get_io(argv):
    fin = sys.stdin
    fout = sys.stdout
    ifn = ofn = "-"
    if len(argv) == 2:
        bfn = sys.argv[1]
        ifn = bfn + '.in'
        ofn = bfn + '.out'
    if len(argv) > 2:
        ifn = argv[1]
        ofn = argv[2]
    if ifn != '-':
        fin = open(ifn, "r")
    if ofn != '-':
        fout = open(ofn, "w")
    return (fin, fout)

def get_numbers():
    line = fin.readline()
    return map(int, line.split())

def get_number():
    return get_numbers()[0]

def get_line():
    line = fin.readline()
    if len(line) > 0 and line[-1] == '\n':
        line = line[:-1]
    return line

def get_string():
    line = fin.readline()
    return line.strip()

def omino(x, r, c):
    rich = 'RICHARD'
    gab = 'GABRIEL'
    ret = rich # default

    # General
    # ew("x=%d, rc=[%d x %d]" % (x, r, c))
    minrc = min(r, c)
    if (r*c) % x != 0:
        ret = rich # cannot fill
    elif max(r, c) < x:
        ret = rich # Long 1xX
    elif x >= 7:
        ret = rich # hole-shape
    elif minrc < (x-1)/2 + 1:
        # ew("L-shape")
        ret = rich # L-shape of radius minrc (with residue)
    else:
        # ew("Non general")
        if x == 1:
            ret = gab
        elif x == 2:
            ret = gab  if (r*c) % 2 == 0 else  rich
        elif x == 3:
            ret = gab  if minrc >= 2 else  rich
        elif x == 4:
            if min(r,c) >= 3 and max(r,c) >= 4:
                ret = gab
            else:
                ret = rich
        elif x == 5:
            if minrc < 3:
                ret = rich  # Khet-shape
        elif x == 6:
            if minrc < 4:
                ret = rich  
            else:
                ret = gab
    return ret

if __name__ == "__main__" and len(sys.argv) == 1 + 3:
    [x, r, c] = map(int, sys.argv[1:])
    sys.stdout.write("(x=%d, r=%d, c=%d): %s\n" %
                     (x, r, c, omino(x, r, c)))
    sys.exit(0)


if __name__ == "__main__":
    (fin, fout) = get_io(sys.argv)
    n_cases = get_number()
    for ci in range(n_cases):
        [x, r, c] = get_numbers()
        r = omino(x, r, c)
        fout.write("Case #%d: %s\n" % (ci + 1, r))

    fin.close()
    fout.close()
    sys.exit(0)
