#!/usr/bin/env python
from sys import stdout

#fin = open("data/sample.in", 'r')
fin = open("data/A-small-attempt1.in", 'r')
#fout = stdout
fout = open("data/a.out", 'w')


# ejp mysljylc kd kxveddknmc re jsicpdrysi
# our language is impossible to understand

# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# there are twenty six factorial possibilities

#de kr kd eoya kw aej tysr re ujdr lkgc jv
#so it is okay if you want to just give up


import string
#t = string.maketrans("abcdefghijklmnopqrstuvwxyz",
#                     "y.e.o....uigl..rz.n..p.ma.")

t = string.maketrans("ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz",
                     "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq")

# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# there are twenty six factorial possibilities

#de kr kd eoya kw aej tysr re ujdr lkgc jv
#so it is okay if you want to just give up
#print "abcdefghijklmnopqrstuvwxyz".translate(t)


cases = int(fin.readline())
for ci in xrange(cases):
    result = fin.readline().strip().translate(t)
    fout.write("Case #%d: %s\n" % (ci+1, result))

