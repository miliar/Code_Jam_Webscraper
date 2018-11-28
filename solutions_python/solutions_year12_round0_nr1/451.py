
enc  =  "ejp mysljylc kd kxveddknmc re jsicpdrysi " \
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd "\
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"

orig =  "our language is impossible to understand "\
        "there are twenty six factorial possibilities "\
        "so it is okay if you want to just give up" 

d={'q':'z', 'z': 'q'}

for ech,ch in zip(enc, orig):
    d[ech] = ch


t = int(raw_input())
for i in xrange(t):
    g = raw_input()
    res = "".join(map(lambda a:d[a], g))
    print "Case #%s: %s" % (i+1, res)
