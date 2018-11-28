import sys
import re

f = open(sys.argv[1], 'r')

T = int(f.readline())

for t in xrange(T):
  R, C = [int(x) for x in f.readline().strip().split()]
  
  floor = []
  for r in xrange(R):
    floor.append(f.readline().strip())
    
  for r in xrange(1, len(floor)):
    for m in re.finditer('##', floor[r]):
      start, end = m.span()
      if floor[r - 1][start:end] == '##':
        floor[r - 1] = floor[r - 1][:start] + '/\\' + floor[r - 1][end:]
        floor[r] = floor[r][:start] + '\\/' + floor[r][end:]
  
  
  impossible = False
  for row in floor:
    if '#' in row:
      impossible = True
      break
      
  print 'Case #%d: ' % (t + 1)
  if impossible:
    print 'Impossible'
  else:
    for row in floor:
      print row

f.close()
