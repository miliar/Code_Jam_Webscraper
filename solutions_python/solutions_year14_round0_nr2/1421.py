#!/usr/bin/env python3
import math
import sys

def main(argv=sys.argv):
    fin, fout = argv[1:3]
    with open(fin) as f, open(fout, 'w') as g:
        T = int(f.readline().strip())
        for i in range(1, T+1):
            rate = 2
            C, F, X = tuple(map(float, f.readline().strip().split()))

            30, 2, 100
            n = max(math.floor((X/C)-(rate/F)), 0)

            result = 0
            for term in range(n):
                result += C/(rate+term*F)

            result += X/(rate+n*F)
            # # 0 farms -> X/rate
            # # 1 farm -> C/rate + X/(rate+F)
            # # 2 farms -> C/rate + C/(rate+F) + X/(rate+2*F)


            # X/(rate+(n-1)*F) vs C/(rate+(n-1)*F) + X/(rate+n*F)

            # (rate+n*F)*X vs C*(rate+n*F)+X(rate+(n-1)*F)
            # X*F vs C*(rate+n*F)

            # n s.t. (X/C)-(rate/F)-1

            # math.floor((X/C)-(rate/F)-1)

            # result = None
            g.write("Case #{}: {}\n".format(i, result))

if __name__ == "__main__":
    status = main()
    sys.exit(status)
