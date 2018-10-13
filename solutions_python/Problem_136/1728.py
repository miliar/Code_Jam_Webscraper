import sys
from decimal import *

input = []

def parse_file(filePath):
    with open(filePath) as f:
        T = int(f.readline())
        for i in range(T):
            input.append(tuple([Decimal(x) for x in f.readline().split()]))

def get_optim_rec(C, F, X, CPS):
    if X/CPS < C/CPS + X/(CPS + F):
        return X/CPS
    return C/CPS + min(X/(CPS + F), get_optim_rec(C, F, X, CPS + F))

def get_optim(C, F, X):
    return str(get_optim_rec(C, F, X, Decimal(2.0)).quantize(Decimal('1.0000000')))

def main():
    parse_file(sys.argv[1])
    getcontext().prec = 10
    sys.setrecursionlimit(15000)
    currTest = 1
    for C, F, X in input:
        print('Case #%d: %s' %(currTest, get_optim(C, F, X)))
        currTest += 1

if __name__ == '__main__':
    main()  
