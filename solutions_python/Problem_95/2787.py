#! /usr/bin/python


# ejp mysljylc kd kxveddknmc re jsicpdrysi
# our language is impossible to understand

# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# there are twenty six factorial possibilities

# de kr kd eoya kw aej tysr re ujdr lkgc jv
# so it is okay if you want to just give up
#        abcdefghijklmnopqrstuvwxyz

from string import maketrans   # Required to call maketrans function.

intab  = "abcdefghijklmnopqrstuvwxyz"
outtab = "yhesocvxduiglbkrztnwjpfmaq" 
trantab = maketrans(intab, outtab)

f = open("test.txt")
nlines = (int)(f.readline())
for i in range(nlines):
    line = f.readline().strip()
    print "Case #%d: %s" % (i+1, line.translate(trantab))

