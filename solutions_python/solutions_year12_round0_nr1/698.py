S = ("ejp mysljylc kd kxveddknmc re jsicpdrysi"+
     "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"+
     "de kr kd eoya kw aej tysr re ujdr lkgc jvzq")
D = ("our language is impossible to understand"+
    "there are twenty six factorial possibilities"+
    "so it is okay if you want to just give upqz")

m = {s:d for s,d in map(lambda x,y:(x,y), S, D)}

N = int(raw_input())

for case in xrange(1, N+1):
    line = raw_input()
    line = "".join(map(lambda x: m[x], line))
    print "Case #%s: %s"%(case, line)
