#!/usr/bin/python 

import string

english = "a zooour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upq"
english += english.upper()
googlerese = "y qeeejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvz"
googlerese += googlerese.upper()

filename = "p1_input.txt"
trans = string.maketrans(googlerese, english)

file = open(filename)
line = file.readline()
for i in xrange(int(line)):
    line = file.readline().rstrip()
    print "Case #" + str(i+1) + ": " + string.translate(line,trans)

