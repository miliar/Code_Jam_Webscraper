#!/usr/bin/env python
# Fair and Square
# count how many palyndromes within a segment.
# Author:  Yotam Medini  yotam.medini@gmail.com -- Created: 2013/April/13
import sys

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

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

# Following values were obtained by manually using
# output from running
#    ./fairsqrlist.py 14
palyndromes = [
                   0,
                   1,
                   4,
                   9,
                 121,
                 484,
               10201,
               12321,
               14641,
               40804,
               44944,
             1002001,
             1234321,
             4008004,
           100020001,
           102030201,
           104060401,
           121242121,
           123454321,
           125686521,
           400080004,
           404090404,
         10000200001,
         10221412201,
         12102420121,
         12345654321,
         40000800004,
       1000002000001,
       1002003002001,
       1004006004001,
       1020304030201,
       1022325232201,
       1024348434201,
       1210024200121,
       1212225222121,
       1214428244121,
       1232346432321,
       1234567654321,
       4000008000004,
       4004009004004,
     100000020000001,
     100220141022001,
     102012040210201,
     102234363432201,
     121000242000121,
     121242363242121,
     123212464212321,
     123456787654321,
     400000080000004,
   10000000200000001,
   10002000300020001,
   10004000600040001,
   10020210401202001,
   10022212521222001,
   10024214841242001,
   10201020402010201,
   10203040504030201,
   10205060806050201,
   10221432623412201,
   10223454745432201,
   12100002420000121,
   12102202520220121,
   12104402820440121,
   12122232623222121,
   12124434743442121,
   12321024642012321,
   12323244744232321,
   12343456865434321,
   12345678987654321,
   40000000800000004,
   40004000900040004,
]                   


def palyndromes_interval_count(A, B):
    "Assuming A < B, count num,ber of palyndromes within [A,B]"
    global palyndromes

    # List is small, so linear search will do.
    np = len(palyndromes)

    # skip small
    b = 0
    while b < np and palyndromes[b] < A:
        b += 1

    # Get to larger
    e = b
    while e < np and palyndromes[e] <= B:
        e += 1
    if e == np:
        sys.stderr.write("I know too few palyndromes...:(\n")
    # sys.stderr.write("b=%d, e=%d\n" % (b, e))
    return e - b

if __name__ == "__main__":
    (fin, fout) = get_io(sys.argv)
    n_cases = get_number()
    for ci in range(n_cases):
        [A, B] = get_numbers()
        r = palyndromes_interval_count(A, B)
        fout.write("Case #%d: %s\n" % (ci + 1, r))

    fin.close()
    fout.close()
    sys.exit(0)
