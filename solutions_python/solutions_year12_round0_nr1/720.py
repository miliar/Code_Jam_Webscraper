import sys

def learn(samples):
    res = dict()
    for x, y in samples:
        assert len(x) == len(y)
        for i in xrange(len(x)):
            if x[i] not in res:
                res[x[i]] = y[i]
            else:
                assert res[x[i]] == y[i], 'was: {0} -> {1}, trying: {2} -> {3}'.format(x[i], res[x[i]], x[i], y[i])
    return res

def decode(s, d):
    return ''.join(map(lambda x: d[x], s))

def main():
    samples = [("y qee", "a zoo"), ("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"), ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"), ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"), ("z", "q")]

    d = learn(samples)
    assert d[' '] == ' '
    for c in map(chr, xrange(ord('a'), ord('z') + 1)):
        assert c in d, '{0} not found'.format(c)
    targets = set([v for k, v in d.iteritems()])
    assert len(targets) == 27 # + ' '
    lines = sys.stdin.readlines()
    T = int(lines[0])
    assert len(lines) == T + 1
    for line_no, line in enumerate(lines[1:]):
        print 'Case #{0}: {1}'.format(line_no + 1, decode(line.strip(), d))

if __name__ == '__main__':
    main()
