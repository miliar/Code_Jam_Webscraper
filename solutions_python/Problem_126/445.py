#! /usr/bin/env python
import sys
import re

sample = "sample"

if len(sys.argv) < 2:
    print "usage: %s [sample | name]" % (sys.argv[0], )
    sys.exit(1)

if sys.argv[1].lower() == "sample":
    fin = open(sample + ".in", "r") 
    fout = open(sample + ".out", "w")
else:
    fin = open(sys.argv[1], "r")
    fout = open(sys.argv[1] + ".out", "w")

case = 1
ncases = int(fin.readline())

def splitstring(s):
    result = []
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            result.append(s[i:j])
    return result

def isvalid(s, n):
    m = 0
    for ch in s:
        if ch not in vowels:
            m += 1
    return True

while True:
    line = fin.readline()
    line = line.rstrip()

    parts = line.split()
    name = parts[0]
    nn = int(parts[1])
    nval = 0

    subs = splitstring(name)
    pattern = r"[^aeiouAEIOU]{%s}" % (str(nn), )
    
    for sub in subs:
        if re.search(pattern, sub):
            nval += 1

    msg = "Case #%d: %d\n" % (case, nval)
    fout.write(msg)
    case += 1

    if case > ncases:
        break

fin.close()
fout.close()
