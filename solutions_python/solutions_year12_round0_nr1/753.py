#!/usr/bin/env python

from sys import stdin
from string import maketrans

source = "y qee" \
    "ejp mysljylc kd kxveddknmc re jsicpdrysi" \
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" \
    "de kr kd eoya kw aej tysr re ujdr lkgc jvz"

target = "a zoo" \
    "our language is impossible to understand" \
    "there are twenty six factorial possibilities" \
    "so it is okay if you want to just give upq"

translationTable = maketrans(source, target)

for case in range (int(stdin.readline())):
    sentence = stdin.readline().rstrip()
    print "Case #%d: %s" % (case + 1, sentence.translate(translationTable))
