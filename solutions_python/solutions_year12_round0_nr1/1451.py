import sys

d=dict(zip(
"""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
y qeez""",
"""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
a zooq"""))
for e in enumerate(input().split('\n')[1:]):
    print("Case #" + str(e[0]+1) + ": " + ''.join([d[x] for x in e[1]]))
