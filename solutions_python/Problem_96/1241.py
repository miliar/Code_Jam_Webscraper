def countBest(s,p,t):
    count = 0
    for i in t:
        if (i+2)/3 >= p:
            count += 1
        elif s and i>1 and (i+4)/3 >= p:
            count += 1
            s -= 1
    return count


if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        ln = map(int, f.readline().strip().split())
        N = ln[0]
        S = ln[1]
        p = ln[2]
        t = ln[3:3+N]
        print 'Case #%d: %d'%(i+1, countBest(S,p,t))

