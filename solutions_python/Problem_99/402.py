import sys
from itertools import combinations as comb
from operator import mul

def solve(A, B, p):
    #print A, B, p

    keeptyping = []
    rightaway = []
    backspace = []
    prob = []

    for i in xrange(A+1):
        for mistakes in comb(xrange(A), i):
            m = p[:]
            for k in mistakes:
                m[k] = 1-m[k]
            prob.append(reduce(mul, m))
            keeptyping.append(B-A+1 + (B+1)*(len(mistakes)>0))
            rightaway.append(B+2)
            bsp = [0]*A
            for i in xrange(A):
                bsp[i] = i+1 + B-A + i+2 + (B+1)*(sum(1 for x in mistakes if x < A-(i+1))>0)
            backspace.append(bsp)
    #print prob, keeptyping, backspace, rightaway

    a = sum(prob[i]*keeptyping[i] for i in xrange(len(prob)))
    b = sum(prob[i]*rightaway[i] for i in xrange(len(prob)))
    c = min(sum(prob[i]*backspace[i][j] for i in xrange(len(prob))) for j in xrange(len(backspace[i])))
    #print a, b, c
    return min(a, b, c)

def main():
    with open(sys.argv[1]) as f:
        T = int(f.readline().strip())
        for i in range(T):
            v = f.readline().split()
            A, B = [int(x) for x in v]
            v = f.readline().split()
            p = [float(x) for x in v]
            res = solve(A, B, p)
            print 'Case #%d: %f' % (i+1, res)

if __name__ == "__main__":
    main()
