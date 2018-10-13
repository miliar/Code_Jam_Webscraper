examples = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"]
trans = ["our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"]

d = {}
d['q'] = 'z'
d['z'] = 'q'
for ind in range(len(examples)) :
    ex = examples[ind]
    tr = trans[ind]
    for j in range(len(ex)) :
        d[ex[j]] = tr[j]

n = int(raw_input())
for i in range(n) :
    line = raw_input()
    newline = 'Case #%d: ' % (i+1)
    for c in line :
        newline += d[c]
    print newline
    
