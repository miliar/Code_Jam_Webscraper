def max_n(C, F, X):
    '''the maximum n that satisfies C/(2+(n-1)F) < X*(1/(2+(n-1)F) - 1/(2+nF))'''
    n = 1
    while C/(2+(n-1)*F) < X*(1/(2+(n-1)*F) - 1/(2+n*F)):
        n += 1
    return n-1

def calc(n, C, F, X):
    cumsum = 0
    for i in range(n):
        cumsum += 1.0/(2+i*F)
    return C*cumsum + X/(2+n*F)



if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    with open(infile) as f:
        T = int(f.readline().strip())
        for i in range(T):
            C, F, X = map(float, f.readline().strip().split())
            n = max_n(C, F, X)
            # print n
            t = calc(n, C, F, X)
            print 'Case #%d: %s'%(i+1, t)
