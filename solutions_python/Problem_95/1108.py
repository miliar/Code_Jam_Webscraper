dst = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

src = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

translate = { 'y': 'a', 'e': 'o', 'q': 'z' }

for s, d in zip(src, dst):
    if d in translate:
        assert translate[d] == s
    else:
        translate[d] = s

missing_d = set('abcdefghijklmnopqrstuvwxyz') - set(translate.values())
missing_s = set('abcdefghijklmnopqrstuvwxyz') - set(translate)

assert len(missing_s) == 1
assert len(missing_d) == 1

translate[missing_s.pop()] = missing_d.pop()
assert len(translate) == 28
assert len(translate.values()) == 28

import sys
L = list(sys.stdin)

for t in range(1, 1+int(L[0])):
    print 'Case #%d: %s' % (t, ''.join(translate[c] for c in L[t][:-1]))                            
