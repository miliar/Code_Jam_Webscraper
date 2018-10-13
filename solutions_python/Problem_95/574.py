import itertools
import string
import sys

def build_mapping():
  g_to_s = {'y':'a', 'e':'o', 'q':'z'}
  gs = ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv')
  ss = ('our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up')
  for (g, s) in itertools.izip(gs, ss):
    for i, l in enumerate(g):
      g_to_s[l] = s[i]
  
  alphabet = string.ascii_lowercase
  for a in alphabet:
    if a not in g_to_s:
      s = list(g_to_s.itervalues())
      missing = [a for a in alphabet if a not in s]
      g_to_s[a] = missing[0]
  return g_to_s
  
def translate(g, mapping):
  return ''.join([mapping[l] for l in g])

if __name__ == '__main__':
  mapping = build_mapping()
  with open(sys.argv[1], 'r') as f:
    t = int(f.readline())
    for j in range(1, t + 1):
      g = f.readline().strip()
      s = translate(g, mapping)
      print 'Case #%d: %s' % (j, s)
