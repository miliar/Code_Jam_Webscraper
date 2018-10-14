mapping = {}
inputs = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""
outputs = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

for i in range(len(inputs)):
    mapping[inputs[i]] = outputs[i]

mapping['q'] = 'z'
mapping['z'] = 'q'

times = int(raw_input())
i = 1
result = []
while i <= times:
    sentence = raw_input()
    process = ""
    for w in sentence:
        process += mapping[w]
    result.append("Case #%d: %s" % (i, process))
    i += 1
for r in result:
    print r
