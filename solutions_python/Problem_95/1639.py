import string

trans = string.maketrans('''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvqz''',
'''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upzq''')

T = int(raw_input())
for i in range(T):
    G = raw_input()
    print "Case #%d: %s" % (i + 1, string.translate(G, trans))
