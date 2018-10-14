n_cases = input()

for case in xrange(1, n_cases + 1):
    n, k = map(int, raw_input().split())

    s = bin(k)[2:][-n:]
#    print n, k, s
    on = len(s) >= n and '0' not in s

    print "Case #%d: %s" % (case, "ON" if on else "OFF")
