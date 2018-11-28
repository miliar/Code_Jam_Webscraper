import sys

def solve(N, S, p, scores):
    #print N,S,p,scores
    result = 0

    for score in scores:
        b = score/3
        rem = score-3*b

        if b >= p:
            result += 1
            #print b,b,b
        elif b+1 >= p and score > 0:
            if rem >= 1:
                result += 1
                #print b+1,b,b
            else:
                if S > 0:
                    result += 1
                    S -= 1
                    #print b+1,b,b-1,' (*)'
        elif b+2 >= p and score > 0:
            if rem >= 2 and S > 0:
                result += 1
                S -= 1
                #print b+2,b,b,' (*)'

    return result

def main():
    with open(sys.argv[1]) as f:
        f.readline()
        for i, line in enumerate(f):
            vals = [int(x) for x in line.strip().split()]
            res = solve(vals[0], vals[1], vals[2], vals[3:])
            print 'Case #%d: %d' % (i+1, res)

if __name__ == "__main__":
    main()
