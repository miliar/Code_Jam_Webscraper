import sys
import os

def getTime(C, F, X):
    t, n = 0, 0
    while True:
        t1 = t + C / (2 + n*F) + X / (2 + (n+1)*F) # time to buy 1 more farm and wait to win
        t2 = t + X / (2 + n*F) # time to just wait to win
        if t1 < t2:
            # buying another farm is efficient
            t += C / (2 + n*F)
            n += 1
        else:
            # just wait
            t = t2
            break
    return t

def main():
    with open(sys.argv[1], 'r') as inp, open('%s.out' % (os.path.splitext(sys.argv[1])[0]), 'w') as out:
        T = int(inp.readline())
        for t in xrange(T):
            C, F, X = [float(x) for x in inp.readline().split()]
            out.write('Case #%s: %.8f\n' % (t + 1, getTime(C, F, X)))

if __name__ == '__main__':
    main()