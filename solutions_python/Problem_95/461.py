a = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
b = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

mapping = {
    'y': 'a',
    'e': 'o',
    'q': 'z',
}

for x, y in zip(a, b):
    if 'a' <= x <= 'z':
        mapping[x] = y

alphabeth = set([chr(x) for x in range(ord('a'), ord('z')+1)])
ex_keys = alphabeth.difference(set(mapping.keys()))
ex_vals = alphabeth.difference(set(mapping.values()))

for x, y in zip(ex_keys, ex_vals):
    mapping[x] = y

print mapping, len(mapping)


with open('A-small-attempt0.in') as f, open('A-small-attempt0.txt', 'w') as fout:
    ncases = int(f.readline())

    for i in range(ncases):
        fout.write("Case #%d: " % (i + 1))
        for x in f.readline():
            try:
                fout.write(mapping[x])
            except KeyError:
                fout.write(x)
