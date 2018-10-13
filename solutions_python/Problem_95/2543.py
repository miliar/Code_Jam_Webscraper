#!/usr/bin/env python
from string import maketrans
from sys import argv, stdin
from pdb import set_trace as debug

orig   = "abcdefghijklmnopqrstuvwxyz"
cipher = "yhesocvxduiglbkrztnwjpfmaq"
trans  = maketrans(orig, cipher)

if __name__ == "__main__":
    lines = stdin.readlines()
    count = 1;
    lines.pop(0)
    for line in lines:
        print "Case #{0}:".format(count), line.translate(trans),
        count += 1
