#!/usr/bin/env python
import sys
import time
import pickle

OUTFILE = sys.stderr
STARTTIME = time.time()

def v(string):
    """Output verbose with a timestamp"""
    t = int(time.time() - STARTTIME)
    print >> sys.stderr, "%s: %s" % (t, string)

def o(string):
    """Send to the outfile"""
    global OUTFILE
    v(string)
    print >> OUTFILE, string

def main(fp):
    numCases = int(fp.readline())
    maps = pickle.load(open("dict.dat", "rb")) #Maps cipher letter to english letter
    v("Num Cases: %s" % (numCases))
    case = 0
    try:
        for line in fp.readlines():
            case += 1
            caseResult = ""
            v(line)
            words = line.strip().split()
            for w in words:
                answer = ""
                valid = False
                while not valid:
                    while len(answer) != len(w) and not valid:
                        unknown, dword = decrypt(w, maps)
                        if unknown > 0:
                            v("Word: %s? " % dword)
                            answer = raw_input()
                        else:
                            answer = dword
                    if len(maps) < 26:
                        valid = add_to_dict(w, answer, maps)
                    else:
                        valid = True
                caseResult += " %s" % (answer)
                v(answer)
            o("Case #%s:%s" % (case, caseResult))




    finally:
        pickle.dump(maps, open("dict.dat", "wb"))






def add_to_dict(encrypt, plaintext, maps):
    assert len(encrypt) == len(plaintext), "Cipher and plaintext not equal! %s, %s, %s" % (encrypt, plaintext, maps)
    valid = True
    for i in range(len(encrypt)):
        if encrypt[i] in maps:
            if plaintext[i].lower() != maps[encrypt[i].lower()]:
                valid = False
                break

    if valid:
        for i, el in enumerate(encrypt):
            maps[el.lower()] = plaintext[i].lower()
        return True
    else:
        return False
    

def decrypt(string, mapping):
    outstr = ""
    unknown = 0
    for letter in string:
        if letter not in mapping:
            unknown += 1
        outstr += mapping.get(letter, letter.upper())
    return unknown, outstr
        

if __name__ == "__main__":
    global OUTFILE
    v("Starting")
    if len(sys.argv) < 2:
        v("Error, need input file as argument")
        exit(1)
    else:
        fname = sys.argv[1]
        OUTFILE = open("OUTPUT_"+fname, "w")
        main(open(fname, "r"))
    v("Finished")
