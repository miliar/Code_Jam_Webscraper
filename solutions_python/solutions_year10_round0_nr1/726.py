# python snapper_chain.py input_file output_file
import sys

def solve(N, K):
    mask = 1
    for i in range(N):
        if not (mask & K): return False
        mask = 2 * mask
    return True

inpath = sys.argv[1]
outpath = sys.argv[2]
fin = open(inpath)
fout = open(outpath, 'w')
T = int(fin.readline().strip())
for i in range(T):
    N, K = (int(s) for s in fin.readline().strip().split())
    state = solve(N, K)
    print >>fout, 'Case #%d: %s' % ((i+1, 'ON' if state else 'OFF'))
fout.close()
