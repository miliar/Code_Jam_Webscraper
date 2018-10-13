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


def standing(shyness_digits):
    invite = 0
    curr_standing = 0
    ew0("shyness_digits=%s" % shyness_digits)
    for shyness in range(len(shyness_digits)):
        n_shyness = int(shyness_digits[shyness])
        ew0("shyness=%d, n_shyness=%d, curr_standing=%d" %
           (shyness, n_shyness, curr_standing))
        if n_shyness > 0:
            if curr_standing < shyness:
                need = shyness - curr_standing
                invite += need
                curr_standing += n_shyness + need
                ew0("need=%d, invite=%d, curr_standing=%d" %
                   (need, invite, curr_standing))
            else:
                curr_standing += n_shyness
                
    return invite


if __name__ == "__main__":
    (fin, fout) = get_io(sys.argv)
    n_cases = get_number()
    for ci in range(n_cases):
        shyness_line = get_string()
        r = standing(shyness_line.split()[1])
        fout.write("Case #%d: %s\n" % (ci + 1, r))

    fin.close()
    fout.close()
    sys.exit(0)
