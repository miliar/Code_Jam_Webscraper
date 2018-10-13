import string

data = {
  "yeq": "aoz",
  "ejp mysljylc kd kxveddknmc re jsicpdrysi": "our language is impossible to understand",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd": "there are twenty six factorial possibilities",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv": "so it is okay if you want to just give up"
}

dic = {}
for k, v in data.items():
  for i in xrange(len(k)):
    dic[k[i]] = v[i]

unknown = list(set(string.lowercase) - set(dic.keys()))
if len(unknown) == 1:
  dic[unknown[0]] = list(set(string.lowercase) - set(dic.values()))[0]

#for c in string.lowercase:
#  print "'%s': '%s'" % (c, dic.get(c, '?'))

T = int(raw_input())
for t in xrange(T):
  G = raw_input()
  print "Case #%i: %s" % (t+1, ''.join(map(lambda c: dic[c], G)))
