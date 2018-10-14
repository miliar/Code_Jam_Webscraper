samples = [['ejp mysljylc kd kxveddknmc re jsicpdrysi',
'our language is impossible to understand'],
['rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
'there are twenty six factorial possibilities'],
['de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up']]

mapping = {'y':'a','o':'e','q':'z'}

for sample in samples:
    for i in range(len(sample[0])):
        if sample[0][i] != " ":
            mapping[sample[0][i]] = sample[1][i]

for k in sorted(mapping.keys()):
   print k, mapping[k]
print mapping
print len(mapping)
