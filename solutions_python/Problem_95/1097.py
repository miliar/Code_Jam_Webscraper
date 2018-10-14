import sys

enc = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
dec = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

mapa = {}

for i in range(0, len(enc)):
  mapa[enc[i]] = dec[i]
mapa['q'] = 'z'
mapa['z'] = 'q'
mapa['\n'] = '\n'

def doit(text, dic):
  l = list(text)
  for i in range(0, len(l)):
    l[i] = dic[l[i]]
  return l

n = int(sys.stdin.readline())
for i in range(0, n):
  s = sys.stdin.readline()
  print "Case #%d: %s" % (i + 1, "".join(doit(s, mapa))),
