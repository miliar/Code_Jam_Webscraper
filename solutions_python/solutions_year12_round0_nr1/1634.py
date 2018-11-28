from string import ascii_lowercase
a="""y qee ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

b="""a zoo our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

table = {"z": "q"}
for i in xrange(len(a)):
    table[a[i]] = b[i]

num = 0
new = []
for line in open("file.txt", "rU"):
    num += 1
    new.append("Case #" + str(num) + ": ")
    for i in xrange(len(line)):
        new.append(table[line[i]])

print "".join(new)
