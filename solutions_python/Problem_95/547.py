#! python

import sys

orig = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', \
  'de kr kd eoya kw aej tysr re ujdr lkgc jv']
prod = ['our language is impossible to understand', 'there are twenty six factorial possibilities', \
  'so it is okay if you want to just give up']

def main(args):
  mapping = dict()
  for i in range(0, 3):
    x = orig[i]
    y = prod[i]
    if (len(x) != len(y)):
      print 'error!';
      continue;
    for k in range(0, len(x)):
      if (x[k] == ' '):
        continue
      if (x[k] in mapping and mapping[x[k]] != y[k]):
        print 'mapping inconsistent'
      else:
        mapping[x[k]] = y[k]

  mapping['q'] = 'z'
  mapping['z'] = 'q'
  print mapping
  print len(mapping)
  print sorted(mapping.values())

  fin = open('input.txt', 'r')
  data = fin.read().split('\n')
  fin.close()
  fout = open('output.txt', 'w')
  fl = data[0]
  data = data[1:]
  n = int(fl)
  idx = 0
  for line in data:
    idx = idx + 1
    if (idx > n):
      break
    res = 'Case #{0}: '.format(str(idx))
    for ch in line:
      if ch == ' ':
        res += ' '
      else:
        res += mapping[ch]
    res += '\n'
    fout.write(res)
  fout.close()

if __name__ == "__main__":
    main(sys.argv[1:])
