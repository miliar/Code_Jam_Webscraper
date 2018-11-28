def find():
  f = open('t1.txt', 'r')
  lines = f.readlines()
  f.close()
  test = lines[1:]
  f = open('o1.txt', 'r')
  lines = f.readlines()
  f.close()
  mapping = {}
  for line in range(len(test)):
    for i in range(len(test[line])):
      fromLetter = test[line][i]
      toLetter = lines[line][i]
      if fromLetter >= 'a' and fromLetter <= 'z':
        mapping.setdefault(test[line][i], lines[line][i])
  mapping['q'] = 'z'
  mapping['z'] = 'q'
  return mapping
    
    
m = find()

def solve(in_file, out_file):
  f = open(in_file, 'r')
  lines = f.readlines()
  f.close()
  res = []
  for l in lines[1:]:
    l = l.strip()
    r = ''
    for c in l:
      if c != ' ':
        r += m[c]
      else:
        r += c
    res.append(r)
  f = open(out_file, 'w')
  i = 1
  for l in res:
    f.write('Case #%d: %s\n' % (i, l))
    i += 1
  f.close()
  print 'Solved'
  
solve('A-small-attempt0.in', 'A-small.out')


