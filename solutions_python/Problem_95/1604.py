#!/usr/bin/python
import sys

txt = { "yeq":"aoz", 
        "ejp mysljylc kd kxveddknmc re jsicpdrysi":"our language is impossible to understand",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd":"there are twenty six factorial possibilities",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv":"so it is okay if you want to just give up"
      }
      
trans = {}
for google, normal in txt.iteritems():
    for i in xrange(min(len(google), len(normal))):
        trans[google[i]] = normal[i]
missing_g = None
missing_n = None
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter not in trans.keys():
        missing_g = letter
    if letter not in trans.values():
        missing_n = letter
if len(trans) == 26: # includes " "
    trans[missing_g] = missing_n
##for pair in sorted(trans.iteritems()):
    ##print pair
##print len(trans)

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
    gline = sys.stdin.readline().strip()
    nline = "".join(trans[ch] for ch in gline)
    print "Case #{0}: {1}".format(test_case, nline)
