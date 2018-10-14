C = [100, 50, 25, 20, 10, 4, 2]

def solve(infile):
    input = open(infile)
    T = int(input.readline())
    for t in xrange(1, T+1):
        N, Pd, Pg = [int(x) for x in input.readline().split()]
        D = 100
        D1 = Pd
        G = 100
        G1 = Pg
        for c in C:
            if Pd % c == 0 and Pd / c <= N:
                D = 100 / c
                D1 = Pd / c
                break
        for c in C:
            if Pg % c == 0 and Pg / c >= D1:
                G = 100 / c
                G1 = Pg / c
                break
        if G >= D and N >= D and G1 >= D1 and G - G1 >= D - D1:
            print "Case #%d:" % t, "Possible"
        else:
            print "Case #%d:" % t, "Broken"
    input.close()

if __name__ == '__main__':
    import sys
    solve(sys.argv[1])
