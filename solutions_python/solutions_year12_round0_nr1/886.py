#!python3
src = "zy qee" + "ejp mysljylc kd kxveddknmc re jsicpdrysi" + "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" + "de kr kd eoya kw aej tysr re ujdr lkgc jv"
dst = "qa zoo" + "our language is impossible to understand" + "there are twenty six factorial possibilities" + "so it is okay if you want to just give up"
assert len(set(src)) == 27
assert len(set(dst)) == 27
assert len(dst) == len(src)

tr = lambda ch: dst[src.index(ch)] if ch in src else str(ord(ch))

import sys
N = int(sys.stdin.readline())
for i in range(N):
    s = sys.stdin.readline().rstrip('\r\n')
    print("Case #%d:" % (i+1), ''.join(tr(ch) for ch in s))
