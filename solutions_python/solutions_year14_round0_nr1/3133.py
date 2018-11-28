br = open('a-small.in')
pw = open('a.out', 'w')

n = int(br.readline())

for t in range(n):
  a = int(br.readline())
  v = [map(int, br.readline().split()) for i in range(4)][a - 1]
  b = int(br.readline())
  w = [map(int, br.readline().split()) for i in range(4)][b - 1]
  u = list(set(v) & set(w))
  if len(u) == 1:
    pw.write(('Case #%d: %d\n') % (t + 1, u[0]))
  elif len(u) > 1:
    pw.write('Case #%d: Bad magician!\n' % (t + 1))
  else:
    pw.write('Case #%d: Volunteer cheated!\n' % (t + 1))
