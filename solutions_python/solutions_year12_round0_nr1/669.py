inf = open("A-small-attempt0.in")
outf = open("A-small-attempt0.out", "w")

sample = (
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    "yeqz"
)

ans = (
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up",
    "aozq"
)

key = {}
for x, y in zip("".join(sample), "".join(ans)):
    key[x] = y

numTests = int(inf.readline().rstrip())
for test in range(numTests):
    out = "".join(map(key.get, inf.readline().rstrip()))
    print("Case #%d: %s" % (test + 1, out), file=outf)

