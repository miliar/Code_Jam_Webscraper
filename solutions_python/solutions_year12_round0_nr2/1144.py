'''
Created on 14.04.2012

@author: max
'''
fi = open('B-large.in', 'r')
fi.readline()
fo = open('output.txt', 'w+')

for i, line in enumerate(fi):
  if not line: continue
  params = [int(p) for p in line.split()]
  surp = params[1]; p = params[2]; scores = params[3:]
  
  counter = 0
  for score in scores:
    if score < p: continue
    rest = score - p; half = rest / 2
    if half >= p:
      counter += 1
    elif half < p:
      if p - half == 1:
        counter += 1
      elif p - half == 2 and surp > 0:
        counter += 1; surp -= 1
        
  print >>fo, 'Case #%i: %i' % (i+1, counter)
  
  
  