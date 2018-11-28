inp = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz\n"
out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq\n"

conv = {}

for i in range(len(inp)):
    conv[inp[i]] = out[i]

fi = open("A-small-attempt0.txt")
fo = open("test.txt", "w")

start = True
o = ''
i = 1
for line in fi:
    if start:
        start = False
        continue
    o += 'Case #' + str(i) + ': '
    i += 1
    for c in line:
        o += conv[c]

fo.write(o)