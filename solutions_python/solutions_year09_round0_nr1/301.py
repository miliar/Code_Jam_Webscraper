import re

l, d, n = map(int, raw_input().split())

def to_re(pat):
    return re.compile('^'+pat.replace('(', '[').replace(')', ']')+'$')

words = [raw_input() for _ in xrange(d)]
pats = map(to_re, [raw_input() for _ in xrange(n)])

for cas, pat in enumerate(pats):
    cnt = 0
    for word in words:
        if pat.match(word):
            cnt += 1
    print 'Case #%i: %i' % (cas+1, cnt)
