#!/usr/bin/python
import sys

def decode(l):
    if l=='a':
        l = 'y'
    elif l=='b':
        l = 'h'
    elif l=='c':
        l = 'e'
    elif l=='d':
        l = 's'
    elif l=='e':
        l = 'o'
    elif l=='f':
        l = 'c'
    elif l=='g':
        l = 'v'
    elif l=='h':
        l = 'x'
    elif l=='i':
        l = 'd'
    elif l=='j':
        l = 'u'
    elif l=='k':
        l = 'i'
    elif l=='l':
        l = 'g'
    elif l=='m':
        l = 'l'
    elif l=='n':
        l = 'b'
    elif l=='o':
        l = 'k'
    elif l=='p':
        l = 'r'
    elif l=='q':
        l = 'z'
    elif l=='r':
        l = 't'
    elif l=='s':
        l = 'n'
    elif l=='t':
        l = 'w'
    elif l=='u':
        l = 'j'
    elif l=='v':
        l = 'p'
    elif l=='w':
        l = 'f'
    elif l=='x':
        l = 'm'
    elif l=='y':
        l = 'a'
    elif l=='z':
        l = 'q'
    return l

def ungooglerese(inpfile, outfile):
    fid = file(inpfile)
    numCases = fid.readline()
    numCases = int(numCases[:-1])

    fidOut = file(outfile, 'w')

    for ca in range(numCases):
        line = fid.readline()
        line = list(line)
        outputline = []
        for l in line:
            outputline.append(decode(l))
        line = "".join(outputline)
        fidOut.write('Case #%d: %s' % (ca+1, line)) 

if __name__ == "__main__":
    ungooglerese(sys.argv[1], sys.argv[2])


