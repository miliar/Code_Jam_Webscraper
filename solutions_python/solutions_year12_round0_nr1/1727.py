import sys

C = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

P = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

m = {'q': 'z', 'z': 'q'}
assert len(C) == len(P)
for i in range(len(C)):
  m[C[i]] = P[i]

sys.stdin.readline()
br = 1
for line in sys.stdin:
  print "Case #" + str(br) + ": " + "".join(map(lambda x : m[x], line)),
  br = br + 1
