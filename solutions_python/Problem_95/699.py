#!/usr/bin/env python

mapping = "ynfi cwlb kuom xsev zpdr jgth aq".replace(" ","")

#reverse mapping
mapping = [(l, i) for i, l in enumerate(mapping)]
mapping.sort()
mapping = "".join(chr(m[1] + ord('a')) for m in mapping)

def decrypt_word(s):
    return "".join(mapping[ord(x)-ord('a')] for x in s)

def decrypt(s):
    return " ".join(decrypt_word(x) for x in s.split(" "))

import sys
f = open(sys.argv[1])
n = int(f.readline())
for i in range(n):
    line = f.readline().strip()
    print "Case #%d: %s" % (i+1, decrypt(line))


    
