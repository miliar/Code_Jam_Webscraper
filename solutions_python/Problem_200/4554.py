
import sys

def isAscOrder(val):
    for i in range(0, len(val)-1):
        if val[i] > val[i+1]:
            return False
    return True

def isTidy(val):
    v = str(val)
    if not isAscOrder(v):
        return False
    if '0' in v:
        return False
    return True

def solv(n):
    for i in range(n, 0, -1):
#        print(i)
        if isTidy(i):
            return i

def main(filename):
    with open(filename, 'r') as f:
        t = int(f.readline())
        for ti in range(1, t+1):
            n = int(f.readline())
            r = solv(n)
            print('Case #{}: {}'.format(ti, r))

if __name__ == '__main__':
    main(sys.argv[1])
