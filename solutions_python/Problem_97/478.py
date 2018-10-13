def read(input_file, out_file):
  f = open(input_file, 'r')
  lines = f.readlines()
  f.close()
  lines = lines[1:]
  f = open(out_file, 'w')
  i = 1
  for l in lines:
    parts = l.strip().split()
    A, B = int(parts[0]), int(parts[1])
    print 'i: ', i, ' ', A, B
    res = solve(A, B)
    f.write('Case #%d: %d\n' % (i, res))
    i += 1
  f.close()
  print 'Solved'
    
def solve(A, B):
  t = set()
  for i in range(A, B + 1):
    a = str(i)
    for j in range(1, len(a)):
      rotated = a[j:] + a[:j]
      r = int(rotated)
      if len(a) == len(str(r)):
        if r <= B and i <= r and i != r:
          t.add((i, r))
  return len(t)
    
read('C-large.in', 'C-large.out') 

