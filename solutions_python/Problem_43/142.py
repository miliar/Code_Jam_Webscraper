"""
Google Code Jam 2009
Round 1C
Challenge: A. All Your Base

By Marcel Rodrigues

Code for Python 2.5+
"""

filename = "A-large"

inpath = filename + ".in"
outpath = filename + ".out"

infile = open(inpath, "r")
outfile = open(outpath, "w")

ncases = int(infile.readline().rstrip())

for case in range(ncases):
    msg = infile.readline().rstrip()
    digits = [msg[0]]
    for dig in msg[1:]:
        if dig not in digits:
            digits.append(dig)
    base = len(digits)
    if base == 1:
        sec = 2 ** len(msg) - 1
        outfile.write("Case #%d: %d\n" % (case + 1, sec))
        continue
    digits[:2] = digits[1::-1]
    sec = 0
    expfactor = 1
    for dig in msg[::-1]:
        sec += digits.index(dig) * expfactor
        expfactor *= base
    outfile.write("Case #%d: %d\n" % (case + 1, sec))

infile.close()
outfile.close()
