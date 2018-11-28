#!/usr/bin/python

a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

d = { 'z': 'q', 'q':'z'}

for i in range(len(a)):
    d[a[i]] = b[i]

print d
keys = d.keys()
keys.sort()
print keys

fp = open('/Users/ryan/Downloads/A-small-attempt1.in')
cases = fp.readline()

c = 1
print "Output"
for line in fp:
    line = line[:-1]
    s = ""
    for i in range(len(line)):
        s = s + d[line[i]]
    print "Case #%d: %s" % (c,s)
    c = c + 1
    

