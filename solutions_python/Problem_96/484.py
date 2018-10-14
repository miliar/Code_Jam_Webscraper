def read():
  f = open('B-large.in', 'r')
  lines = f.readlines()
  f.close()
  N = int(lines[0].strip())
  f = open('B-large.out', 'w')
  i = 1
  for l in lines[1:]:
    parts = l.strip().split()
    numbers = [int(p) for p in parts]
    res = solve(numbers[1], numbers[2], numbers[3:])
    f.write('Case #%d: %d\n' % (i, res))
    i += 1
  f.close()
  print 'Solved'
    
    
def solve(S, p, a):
  m = p + 2 * (p - 1)
  mS = p + 2 * max(0, (p - 2))
  total = 0
  for x in a:
    if x < m and x >= mS and S > 0:
      total += 1
      S -= 1
    if x >= m:
      total += 1
  return total
  
  
read()
