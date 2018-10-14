keystr = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
zq
"""

transstr = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
qz
"""

trans = dict([(a,b) for a,b in zip(keystr,transstr)])

a = open('A-small-attempt0.in')


for i,line in enumerate(a):
    if i==0: continue
    outstring = "".join([trans[x] for x in line[:-1]])
    print "Case #%s: %s" % (i,outstring)
