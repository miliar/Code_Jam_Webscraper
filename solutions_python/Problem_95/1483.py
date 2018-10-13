translations = (
                ('a zoo', 'y qee'),
                ('our language is impossible to understand', 'ejp mysljylc kd kxveddknmc re jsicpdrysi'),
                ('there are twenty six factorial possibilities', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'),
                ('so it is okay if you want to just give up', 'de kr kd eoya kw aej tysr re ujdr lkgc jv'))

mapping = {}

for english,googlese in translations:
    i = 0
    for g in googlese:
        mapping[g] = english[i]
        i = i+1
mapping['z'] = 'q'

def translate(s):
    result = ''
    for c in s:
        try:
            result += mapping[c]
        except:
            pass
    return result

f = open('input', 'r')
out = open('output', 'w')
f.readline()
i = 1
for l in f:
    out.write("Case #%d: %s\n" % (i, translate(l)))
    i += 1