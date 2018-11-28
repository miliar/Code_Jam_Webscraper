import sys
from array import array

def solve_case(line, fout):
    parts = line.split()
    C = int(parts[0])
    combis = {}
    for p in parts[1:C+1]:
        combis[p[:2]] = p[2]
        combis[p[1::-1]] = p[2]
    D = int(parts[C+1])
    opps = {}
    for p in parts[C+2:C+2+D]:
        for c1, c2 in (p, p[::-1]):
            if c1 in opps:
                opps[c1].append(c2)
            else:
                opps[c1] = [c2]
    adds = parts[-1]

    els = array('c')
    for add in adds:
        els.append(add)
        if len(els) < 2: continue
        combid = False
        while els[-2:].tostring() in combis:
            rep = combis[els[-2:].tostring()]
            els.pop()
            els[-1] = rep
            combid = True
        if not combid and add in opps:
            for o2 in opps[add]:
                if o2 in els:
                    els = array('c')
                    break

    return '[%s]' % (', '.join(el for el in els))


def test():
    inpath, outpath = 'test.in', 'test.out'
    fin = open(inpath)
    line = fin.readline().strip()
    line = fin.readline().strip()
    line = fin.readline().strip()
    line = fin.readline().strip()
    fin.close()

def main(inpath, outpath):
    fin = open(inpath)
    T = int(fin.readline().strip())
    fout = open(outpath, 'w')
    for t in range(T):
        print >>fout, 'Case #%d: %s' % (t+1, solve_case(fin.readline().strip(), fout))
    fin.close()
    fout.close()


main(sys.argv[1], sys.argv[2])
