a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
b = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

d = {}
for x,y in zip(a,b):
  d[x] = y

d['z'] = 'q'
d['q'] = 'z'

#for x, y in sorted(d.items()):
#  print '%s\t%s' % (x, y)
t = file('input').readlines()
t = t[1:]
for c, line in enumerate(t):
  line = line[:-1]
  out = ['Case #%d: ' % (c+1)]
  for char in line:
    out.append(d[char])
  print ''.join(out)




