e = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee'
d = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo'
k = dict(zip(e, d))

alpha = set(map(chr, range(ord('a'), ord('z')+1)))
k.update(dict(zip(alpha - set(k.keys()), alpha - set(k.values()))))

for t in range(int(raw_input())):
    print "Case #%d: %s" % (t+1, ''.join(map(lambda c: k[c], raw_input())))
