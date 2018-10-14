import itertools

f = open('C-small.in','r')
fo = open('C-small.out','w')
cases = int(f.readline())

def isRecycled(pair):
  first = pair[0]
  if first == pair[1]:
    return True
  for i in range(1, len(first)):
    if (first[i:] + first[:i] == pair[1]):
      return True
  return False

for case in range(1, cases+1):
  line = f.readline()[:-1]
  items = line.split(' ')
  A = int(items[0])
  B = int(items[1])

  count = 0
  for n in range(A, B+1):
    for m in range(n+1, B+1):
      strn = str(n)
      strm = str(m)
      if (len(strm) > len(strn)):
        break
      if (isRecycled((strn, strm))):
        count += 1

  fo.write('Case #{}: {}\n'.format(case, count))
  print 'Case #{}'.format(case)

f.close()
fo.close()
