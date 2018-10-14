import sys


known = [
    ('a zoo', 'y qee'),
    ('our language is impossible to understand',
        'ejp mysljylc kd kxveddknmc re jsicpdrysi'),
    ('there are twenty six factorial possibilities',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'),
    ('so it is okay if you want to just give up',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv')
]

known = [(one.replace(' ', ''), two.replace(' ', '')) for one, two in known]

mapping = {}

for two, one in known:
    if len(one) != len(two):
        raise Exception('Different lengths: "%s" and "%s"' % (one, two))
    for i in range(len(one)):
        a, b = one[i], two[i]
        if mapping.get(a, b) != b:
            raise Exception('Two replacements for "%s": "%s" and "%s"' %
                    (a, mapping[a], b))
        mapping[a] = b

if len(mapping) < 26:
    s1 = set(''.join([two for one, two in known]))
    s2 = set(''.join([one for one, two in known]))
    if len(s1) == 25:
        ul = ''
        for c in range(97, 123):
            if chr(c) not in s1:
                ul = chr(c)
                break
        if ul:
            for c in range(97, 123):
                if chr(c) not in s2:
                    mapping[ul] = chr(c)
                    break

mapping[' '] = ' '

cases = int(sys.stdin.readline())
for i in range(cases):
    orig = sys.stdin.readline().strip()
    trans = ''
    for c in orig:
        trans += mapping[c]
    print 'Case #%d: %s' % (i + 1, trans)


