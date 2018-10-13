import sys

g2emap = {}
g2emap['y'] = 'a'
g2emap['e'] = 'o'
g2emap['q'] = 'z'

g2emap['z'] = 'q'

goo1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
eng1 = 'our language is impossible to understand'
goo2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
eng2 = 'there are twenty six factorial possibilities'
goo3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
eng3 = 'so it is okay if you want to just give up'

# Create a map from our knowledge of the language
for i in range(len(goo1)):
  if goo1[i] == ' ':
    continue
  if goo1[i] not in g2emap.keys():
    g2emap[goo1[i]] = eng1[i]
  else:
    assert g2emap[goo1[i]] == eng1[i]

for i in range(len(goo2)):
  if goo2[i] == ' ':
    continue
  if goo2[i] not in g2emap.keys():
    g2emap[goo2[i]] = eng2[i]
  else:
    assert g2emap[goo2[i]] == eng2[i]

for i in range(len(goo3)):
  if goo3[i] == ' ':
    continue
  if goo3[i] not in g2emap.keys():
    g2emap[goo3[i]] = eng3[i]
  else:
    assert g2emap[goo3[i]] == eng3[i]

ncases = int(sys.stdin.readline())
for case in range(1, ncases+1):
  current = sys.stdin.readline()
  for i in range(len(current)):
    if current[i] == ' ':
      continue
    elif current[i] in g2emap.keys():
      current = current[:i] + g2emap[current[i]] + current[i+1:]
  print 'Case #' + str(case) + ': ' + current.rstrip()
