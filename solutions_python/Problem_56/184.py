"""
Google Code Jam 2010
Round 1A
Challenge: A. Rotate

By Marcel Rodrigues

Code for Python 2.x
"""

#filename = "sample"
filename = "A-small-attempt1"
#filename = "A-large"

inpath = filename + ".in"
outpath = filename + ".out"

trans = {0: "Neither",
         1: "Red",
         2: "Blue",
         3: "Both"}

infile = open(inpath, "r")
outfile = open(outpath, "w")

def fall(s, N):
    queue = [c for c in s if c != '.']
    e = '.' * (N - len(queue))
    return e + ''.join(queue)

def rows():
    N, K = infile.readline().rstrip().split()
    N, K = int(N), int(K)
    matchR = 'R' * K
    matchB = 'B' * K
    in_a_row = 0
    boardV = [None] * N
    raws = [infile.readline().rstrip() for y in range(N)]
    for y in range(N):
        raw = fall(raws[y], N)
        if not in_a_row & 1:
            if raw.count(matchR):
                in_a_row |= 1
        if not in_a_row & 2:
            if raw.count(matchB):
                in_a_row |= 2
        if in_a_row == 3:
            return 3
        boardV[y] = raw
    boardH = [None] * N
    for y in range(N):
        raw = ''.join([r[y] for r in boardV])
        if not in_a_row & 1:
            if raw.count(matchR):
                in_a_row |= 1
        if not in_a_row & 2:
            if raw.count(matchB):
                in_a_row |= 2
        if in_a_row == 3:
            return 3
        boardH[y] = raw
    boardD1 = [raw[shift:] + raw[:shift] for raw, shift in zip(boardV, range(N))]
    for y in range(N):
        raw = ''.join([r[y] for r in boardD1])
        if not in_a_row & 1:
            if raw.count(matchR):
                in_a_row |= 1
        if not in_a_row & 2:
            if raw.count(matchB):
                in_a_row |= 2
        if in_a_row == 3:
            return 3
    boardD2 = [raw[-shift:] + raw[:-shift] for raw, shift in zip(boardV, range(N))]
    for y in range(N):
        raw = ''.join([r[y] for r in boardD2])
        if not in_a_row & 1:
            if raw.count(matchR):
                in_a_row |= 1
        if not in_a_row & 2:
            if raw.count(matchB):
                in_a_row |= 2
        if in_a_row == 3:
            return 3
    return in_a_row

ncases = int(infile.readline().rstrip())

for case in range(ncases):
    #print case + 1
    in_a_row = rows()
    state = trans[in_a_row]
    out = "Case #%d: %s" % (case + 1, state)
    #print out
    outfile.write(out + '\n')

infile.close()
outfile.close()
