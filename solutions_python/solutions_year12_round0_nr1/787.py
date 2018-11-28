import sys

m = {'a' : 'y', 'o' : 'e', 'z' : 'q'}

inputs = [
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
]

outputs = [
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up",
]

for i in range(3):
    for j in range(len(inputs[i])):
        m[inputs[i][j]] = outputs[i][j]

print m
print len(m.keys())
print sorted(m.values())
m['q'] = 'z'

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    print "Case #%d: %s" % (i, "".join([m[x] for x in line.strip()]))
