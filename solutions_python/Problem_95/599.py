# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import os
import sys
from itertools import chain

data = [("ejp mysljylc kd kxveddknmc re jsicpdrysi",
         "our language is impossible to understand"),
        ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
         "there are twenty six factorial possibilities"),
        ("de kr kd eoya kw aej tysr re ujdr lkgc jv",
         "so it is okay if you want to just give up"),
        ("y qee", "a zoo")]

alphabet = dict.fromkeys(map(chr, xrange(97, 123)), 0)
alphabet["z"] = "q"  # deduction, boss :)x
for enc, dec in data:
    for i, ch in enumerate(enc):
        alphabet[ch] = dec[i]

def translate(line):
    return "".join(alphabet.get(ch, ch) for ch in line)


if __name__ == "__main__":
    n = int(raw_input())
    for i in xrange(1, n + 1):
        line = raw_input()
        print("Case #{0}: {1}".format(i, translate(line)))
