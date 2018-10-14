import string
import sys

sin = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

fr = ""
to = ""
for (i,o) in zip(sin,out):
    if i not in fr:
        fr += i
        to += o
fr += 'q' # given in the problem
to += 'z'
fr += 'z' # q is the only letter remaning for z to map to
to += 'q'

trans = string.maketrans(fr, to)

f = open('A-small-attempt0.in', 'r')
data = f.readlines()
i = 0
for line in data[1:]:
    i += 1
    print "Case #%d: %s" % (i, string.translate(line, trans)),
