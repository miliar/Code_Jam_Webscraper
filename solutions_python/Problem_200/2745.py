#/usr/bin/env python3


FILENAME = 'B-large'
INFILENAME = FILENAME + '.in'
OUTFILENAME = FILENAME + '.out'

def is_good(w : list):
    prev = 0
    for idx, d in enumerate(w):
        if d < prev:
            return False, idx
        prev = d
    return True, None

def solve(w : str):
    ds = list(map(int, list(w)))
    b, d = is_good(ds)
    while True:
        b, d = is_good(ds)
        if b: break
        ds[d - 1] -= 1
        for i in range(d, len(ds)):
            ds[i] = 9
    return "".join(map(str, ds)).lstrip('0')


with open(INFILENAME) as infile, open(OUTFILENAME, 'w') as outfile:
    t = int(infile.readline())
    for i in range(t):
        w = infile.readline().strip()
        x = solve(w)
        outfile.write('Case #{0}: {1}\n'.format(i + 1, x))