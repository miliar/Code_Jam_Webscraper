import math
import sys

def main():
    infile, outfile = sys.argv[1:3]
    with open(infile, 'r') as inp:
      with open(outfile, 'w') as out:
        T = int(inp.readline())
        for case in range(1, T+1):
            (C, F, X) = (float(i) for i in inp.readline().split())
            out.write('Case #{}: '.format(case))
            out.write('{}\n'.format(find_solution(C, F, X)))

def find_solution(C, F, X):
    V = 2.0
    S = 0
    while True:
        tx = X/V
        tf = C/V + X/(V+F)
        if tf < tx:
            # build a farm
            S += C/V
            V += F
        else:
            # don't build
            S += X/V
            break
    return S

if __name__ == '__main__':
    main()
