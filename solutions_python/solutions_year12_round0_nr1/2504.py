
T = {}
for a, b in zip(
        'a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up',
        'y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
    ):
    T[b] = a

import string
T[next(iter(set(string.ascii_lowercase) - set(T.keys())))] = \
    next(iter(set(string.ascii_lowercase) - set(T.values())))

for tt in xrange(int(raw_input())):
    print 'Case #%d: %s' % (tt + 1, ''.join(T[i] for i in raw_input()))
