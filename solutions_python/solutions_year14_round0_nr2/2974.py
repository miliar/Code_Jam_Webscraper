def process(tc):
    c, f, x = [float(s) for s in raw_input().split()]
    capital = 0.0
    best = 987654321
    for i in xrange(1000000):
        best = min(best, capital + x/(2 + i * f))
        capital += c/(2 + i * f)
    print "Case #%d: %.7f" % (tc, best)

if __name__ == "__main__":
    cases = int(raw_input())
    for tc in xrange(1, cases + 1):
        process(tc)
