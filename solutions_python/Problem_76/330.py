import sys
from functools import reduce
filein, fileout = sys.argv[1:3]

def solve(n, xs):
    return "NO" if reduce(lambda x,y: x^y, xs) != 0 else sum(xs) - min(xs)

if __name__ == '__main__':
    with open(filein, 'rU') as f1, open(fileout, 'w') as f2:
        T = int(f1.readline())
        for case in range(T):
            n = int(f1.readline())
            xs = [int(x) for x in f1.readline().strip().split()]
            f2.write("Case #{}: {}\n".format(case+1, solve(n,xs)))
