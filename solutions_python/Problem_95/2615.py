def main():
    training_in = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
    training_out = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'
    d = {}
    for c, c2 in zip(training_in, training_out):
        if c not in d:
            d[c] = c2
    d['q'] = 'z'
    d['z'] = 'q'
    T = int(raw_input())
    for t in xrange(T):
        line = raw_input().strip()
        print "Case #%d:" % (t + 1) + " " + ''.join(d[c] for c in line)

main()
