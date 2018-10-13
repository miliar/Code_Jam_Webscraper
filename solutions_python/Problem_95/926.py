count = input()

abc = 'abcdefghijklmnopqrstuvwxyz '
enc = 'ynficwlbkuomxsev_pdrjgthaq '
enc = 'ynficwlbkuomxsevzpdrjgthaq '

def decode(s):
  return ''.join(abc[enc.find(c)] for c in s)

for i in range(count):
  print 'Case #%s: ' % (i+1) + decode(raw_input())
