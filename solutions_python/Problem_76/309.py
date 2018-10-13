import sys
si = sys.stdin

T = int(si.readline())

def binlist(n):
    re = []
    while n >= 1:
        re.append(n % 2)
        n /= 2

    return re

for tcase in range(T):
    line = si.readline()
    N = int(line)
    values = si.readline()
    values = map(int, values.split())

    bls = map(binlist, values)
    tally_width = max(map(len, bls))
    tally = [0] * tally_width
    for b in bls:
        for i, bit in enumerate(b):
            tally[i] += bit

    no = False
    for i in range(tally_width):
        if tally[i] % 2 == 1:
            no = True
            break

    if no:
        print "Case #%d: NO" % (tcase+1)
    else:
        values.sort()
        sean = sum(values[1:])
        print "Case #%d: %d" % (tcase+1, sean)
    
    
