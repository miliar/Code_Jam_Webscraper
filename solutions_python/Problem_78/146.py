import sys
import fractions

def solve_case(line):
    parts = line.split()
    N, PD, PG = (int(p) for p in parts)
    minD = 100 / fractions.gcd(PD, 100)
    if minD > N: return 'Broken'
    if (PG == 0 or PG == 100) and (PD != PG): return 'Broken'
    return 'Possible'

def test():
    inpath, outpath = 'sample.in', 'sample.out'
    fin = open(inpath)
    line = fin.readline().strip()
    line = fin.readline().strip()
    fin.close()

def main(inpath, outpath):
    fin = open(inpath)
    T = int(fin.readline().strip())
    fout = open(outpath, 'w')
    for t in range(T):
        print >>fout, 'Case #%d: %s' % (t+1, solve_case(fin.readline().strip()))
    fin.close()
    fout.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
