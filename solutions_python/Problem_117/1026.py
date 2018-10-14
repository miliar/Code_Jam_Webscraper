import math
import time
start_time = time.time()

filename = 'B-small-attempt2'
def getvalues():
  fp = open('%s.in' % filename, 'r')
  n = fp.readline().strip('\r\n')
  c = 0
  patterns = []
  for line in fp:
    n, m = line.strip('\r\n').split(' ')
    n, m = int(n), int(m)
    x = 0
    pattern = []
    pc = 1
    for l in fp:
      tempp = l.strip('\r\n').split(' ')
      new_tempp = []
      for temp in tempp:
        if temp == '1':
          new_tempp.append(pc)
        pc += 1
      pattern.extend(new_tempp)
      x += 1
      if x >= n:
        break
    patterns.append([pattern, n, m])
  return patterns

def getcombination(n, m):
  combs = []
  for i in xrange(n):
    comb1 = []
    for j in xrange(m):
      comb1.append(j + (i * m) + 1)
    combs.append(comb1)
  for i in xrange(m):
    comb2 = []
    for j in xrange(n):
      comb2.append(i + (j * m) + 1)
    combs.append(comb2)
  return combs

def generate():
  values = getvalues()
  print values
  result = []
  c = 1
  for value in values:
    combs = getcombination(value[1], value[2])
    done = []
    for comb in combs:
      if len(value[0]) >= len(comb) and len(set(comb).intersection(value[0])) in (value[1], value[2]):
        print comb
        done.extend(comb)
    done = set(done)
    print len(done), len(value[0])
    if len(done) == len(value[0]):
      result.append('Case #%s: %s - %s,%s' % (c, 'YES', value[1], value[2]))
    else:
      result.append('Case #%s: %s - %s,%s' % (c, 'NO', value[1], value[2]))
    c += 1
  return result

xy = generate()
print '\n'.join(xy)
fp = open('%s_out.txt' % filename, 'w')
fp.write('\n'.join(xy))
fp.close()
print time.time() - start_time, "seconds"
