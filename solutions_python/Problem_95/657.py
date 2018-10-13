a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
d = {}
sa = a.split()
sb = b.split()
for i in xrange(len(sa)):
    for j in xrange(len(sa[i])):
        d[ sa[i][j] ] = sb[i][j]
d['z'] = 'q'
d['q'] = 'z'
d[' '] = ' '
#for ch in [chr(i) for i in range(97, 123)]:
#    if ch not in d:
#        print '111111 ', ch
#    if ch not in d.values():
#        print '222222 ', ch
for cas in range(1, int(raw_input()) + 1):
    print 'Case #%d: %s' % (cas, ''.join([d[ch] for ch in raw_input()]))
