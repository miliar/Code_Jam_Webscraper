
def solve(line):
  line.reverse()
  C = int(line.pop())
  trs = dict()

  for i in xrange(0, C):
    tr = line.pop()
    trs[tr[:2]] = tr[2]
    trs[tr[1::-1]] = tr[2]

  D = int(line.pop())
  ops = dict()

  for i in xrange(0, D):
    op = line.pop()

    if op[0] not in ops:
      ops[op[0]] = set()
    if op[1] not in ops:
      ops[op[1]] = set()

    ops[op[0]].add(op[1])
    ops[op[1]].add(op[0])

  line.pop()
  inp = line.pop()

  magicka = []
  for c in inp:
    magicka.append(c)
    last = c
    
    while True:
      ending = ''.join(magicka[-2:])
      if ending in trs:
        last = trs[ending]
        magicka[-2:] = [last]
      else:
        break

    letters = set(magicka)
    if (last in ops) and (not ops[last].isdisjoint(letters)):
      magicka = []


  return ', '.join(magicka)

  
f = open('p1-2inp.txt')
cases = int(f.readline())
for i in xrange(0, cases):
  cur = f.readline()
  res = solve(cur.split())
  print 'Case #%d: [%s]' % (i+1, res)
