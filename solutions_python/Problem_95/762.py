import sys

src = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz"
trg = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq"


T = int(sys.stdin.readline())

def translate(s):
  res = ''
  for c in s:
    i = src.find(c)
    if i == -1:
      print "Nie ma mapowania na:", c
      sys.exit(0)
    res += trg[i]
  return res

for t in range(1, T+1):
  line = sys.stdin.readline().strip()
  print "Case #%d: %s" % (t, translate(line))

