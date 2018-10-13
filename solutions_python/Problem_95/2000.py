s = "ejp mysljylc kd kxveddknmc re jsicpdrysi" +\
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" +\
    "de kr kd eoya kw aej tysr re ujdr lkgc jv" + "zq"
o = "our language is impossible to understand" +\
    "there are twenty six factorial possibilities" +\
    "so it is okay if you want to just give up" + "qz"

d = {}
for i in range(len(s)):
    d[s[i]] = o[i]

N = int(raw_input())
for c in range(1, N+1):
    g = raw_input()
    if not g:
        exit()
    s = ""
    for i in g:
        s += d[i]
    print "Case #%d: %s" % (c, s)