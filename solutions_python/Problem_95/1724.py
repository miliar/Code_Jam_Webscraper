import sys, string

M = string.maketrans("""yeqz
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv""",
"""aozq
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up""")

I = open(sys.argv[1], 'r')
cnt = 0
for line in I:
    if cnt > 0: print ("Case #%d: " % cnt) + line.translate(M)[:-1]
    cnt += 1
I.close()

