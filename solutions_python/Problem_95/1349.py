import sys

with open(sys.argv[1]) as r:
    data = r.read().split('\n')

cipher = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'

plain =  'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'


d = {}

for c, p in zip(cipher, plain):
    d[c] = p

d['q'] = 'z'
d['z'] = 'q'

data = data[1:]

with open('out.txt', 'wb') as w:
    i = 1
    for line in data:
        s = ''.join(d[c] for c in line)
        w.write('Case #%d: %s\n' % (i, s))
        i += 1



