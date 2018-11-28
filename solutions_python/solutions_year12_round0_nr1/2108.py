googlerese = list("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv zq")

english = list("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up qz")

mapping = {}
for i in range(0, len(english)):
    mapping[googlerese[i]] = english[i]

import sys
numCases = int(sys.stdin.readline())
for i in range(1, numCases + 1):
    googlerese_line = list(sys.stdin.readline().rstrip())
    result = ""
    for c in googlerese_line:
        result = result + mapping[c]
    print "Case #" + str(i) + ": " + result
    



