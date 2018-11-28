'''
Created on 14.04.2012

@author: max
'''
fi = open('C-small-attempt0.in', 'r')
fi.readline()
fo = open('output.txt', 'w+')

for j, line in enumerate(fi):
  if not line: continue
  
  A, B = [int(e) for e in line.split()]
  out = []
  
  for n in xrange(A, B+1):
    for m in xrange(n+1, B+1):
      ns = str(n); ms = str(m)
      nlen = len(ns);
      if nlen != len(ms): continue
      for i in range(1, nlen):
        if ns[i] == '0': continue
        if ns[i:] + ns[0:i] == ms:
          out.append((ns, ms))
  
  print >>fo, 'Case #%i: %i' % (j+1, len(set(out)))