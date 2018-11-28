m = dict()

m['y'] = 'a'
m['e'] = 'o'
m['q'] = 'z'
m['z'] = 'q'

after = [
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"]

before = [
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"]

for a,b in zip(after, before):
  for i in range(len(a)):
    m[a[i]] = b[i]


import sys

test = sys.stdin.readlines()
test.pop(0)
for i, t in enumerate(test):
  trans = "".join([m[x] for x in t.strip()])
  print "Case #%d: %s" % (i+1, trans)

