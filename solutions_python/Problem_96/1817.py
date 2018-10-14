

def solve(s, p, scores):
    """
    s - surprising scores
    p - best result seeked
    @return number of googers with best results
    """
    num = 0
    for score in scores:
        mod = score % 3
        if   score < 3:
            result = score
        elif mod == 0:
            result = score / 3
        else: # mod 1 or 2
            result = score / 3 + 1

        if   result >= p:
            num = num + 1
        elif score >= 3 and s > 0 and result == p - 1 and mod != 1: # with mod == 1, you can't get surprising scores
            # in this case we upgrade to a surprising case :)
            num = num + 1
            s = s - 1
    return num

def main():
    tc = "B-small-attempt0"
    f = open("%s.in" % (tc))
    outf = open("%s.out" % (tc), "w")
    T = int(f.readline())

    for i in xrange(1, T + 1):
        scores = [int(x) for x in f.readline().split()]
        N, S , p = scores[0:3]
        del scores[0:3]
        print "Case #%d:" % (i), solve(S, p, scores)
        outf.write("Case #%d: %d\n" % (i, solve(S, p, scores)))
    f.close()
    outf.close()

if __name__ == '__main__':
    main()
