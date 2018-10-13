simbolos = {}

def learn(str1, str2):
  for i in range(0, len(str1)):
    simbolos[str1[i]] = str2[i]

def translate(cadeia):
  result = ""
  for c in cadeia:
    if not (c in simbolos):
      print '$$$$$ ' + c
      result = result + c
    else:
      result = result + simbolos[c]
  return result

learn("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
learn( "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", \
    "there are twenty six factorial possibilities")
learn("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")
learn('qz', 'zq')

import sys
t = int(sys.stdin.readline())
for i in range(1, t+1):
  cadeia = sys.stdin.readline()
  cadeia = cadeia[:len(cadeia)-1]
  print "Case #%d: %s" % (i, translate(cadeia))

