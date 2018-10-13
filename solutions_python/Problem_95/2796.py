train = [("ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "our language is impossible to understand"),
 ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "there are twenty six factorial possibilities"),
 ("de kr kd eoya kw aej tysr re ujdr lkgc jv",
  "so it is okay if you want to just give up")]

m = {}

m["q"] = "z"
m["z"] = "q"

for crypt, plain in train:
    for c, p in zip(crypt, plain):
        if c not in m:
            m[c] = p
        else:
            assert m[c] == p

for k, v in sorted(m.iteritems()):
    print k,"->",v

name = "A-small-attempt0.in"
outname = name[:-3] + ".out"
data = file(name)
count = int(data.readline())
with file(outname, "wb") as out:
    for n, line in enumerate(data):
        plain = ''
        for char in line.strip():
            plain += m[char]
        out.write("Case #%d: %s\n" % (n+1, plain))
    


