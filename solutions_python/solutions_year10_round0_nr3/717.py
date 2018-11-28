# python snapper_chain.py input_file output_file
import sys

def solve(R, k, N, g):
    if sum(g) <= k:
        return sum(g) * R
    else:
        # (num riders, next line position) for each line position
        twolines = g + g
        lps = []
        start, end, riders = 0, 0, 0
        while len(lps) < N:
            if riders + twolines[end] <= k:
                riders += twolines[end]
                end += 1
            else:
                lps.append((riders, end % N))
                riders -= twolines[start]
                start += 1
        euros = 0
        lp = 0
        for i in xrange(R):
            info = lps[lp]
            euros += info[0]
            lp = info[1]
        return euros

inpath = sys.argv[1]
outpath = sys.argv[2]
fin = open(inpath)
fout = open(outpath, 'w')
T = int(fin.readline().strip())
for i in range(T):
    R, k, N = (int(s) for s in fin.readline().strip().split())
    g = [int(s) for s in fin.readline().strip().split()]
    sol = solve(R, k, N, g)
    print >>fout, 'Case #%d: %d' % ((i+1, sol))
fout.close()

