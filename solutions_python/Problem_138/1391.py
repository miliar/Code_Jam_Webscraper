#!/usr/bin/env python3
import bisect
import math
import sys
from decimal import Decimal

def main(argv=sys.argv):
    fin, fout = argv[1:3]
    with open(fin) as f, open(fout, 'w') as g:
        T = int(f.readline().strip())
        for i in range(1, T+1):
            N = int(f.readline().strip())
            naomi_masses = tuple(
                sorted(map(Decimal, f.readline().strip().split())))
            ken_masses = tuple(
                sorted(map(Decimal, f.readline().strip().split())))

            assert len(naomi_masses) == N
            assert len(ken_masses) == N

            # hacking the rules
            ns = list(naomi_masses)
            ks = list(ken_masses)
            cheat_score = 0
            for curr in ns:
                if curr < ks[0]:
                    del ks[-1]
                else:
                    cheat_score += 1
                    del ks[0]


            # following the rules
            ns = list(naomi_masses)
            ks = list(ken_masses)

            good_score = 0
            while ns:
                curr_n = ns.pop()
                if curr_n > ks[-1]:
                    good_score += 1
                    del ks[0]
                else:
                    index = bisect.bisect(ks, curr_n)
                    del ks[index]

            g.write("Case #{}: {} {}\n".format(i, cheat_score, good_score))

if __name__ == "__main__":
    status = main()
    sys.exit(status)
