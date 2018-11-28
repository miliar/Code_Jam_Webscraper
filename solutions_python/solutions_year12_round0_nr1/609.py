import sys
IN="""
y qee
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""
OUT="""
a zoo
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

only_letters = lambda x: x >= 'a' and x <= 'z'
i = filter(only_letters, IN)
o = filter(only_letters, OUT)
trans = dict(zip(i, o))
missingk = sum(xrange(ord('a'), ord('z') + 1))
missingv = missingk
for k, v in trans.items():
    missingk -= (ord(k))
    missingv -= (ord(v))
trans[chr(missingk)] = chr(missingv)

lines = sys.stdin.readlines()

idx = 1
for l in lines[1:]:
    s = ''
    print 'Case #{0}:'.format(idx),
    idx += 1
    for i in l:
        if i in trans:
            s += trans[i]
        else:
            s += i
    print s,




