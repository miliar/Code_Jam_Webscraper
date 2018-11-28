def get_last_person_spread(N, k):
  a = (N-1)/2
  b = N-1 - a
  if k == 1:
    return b, a
  k1 = (k-1)/2
  k2 = k-1 - k1
  if k1 == k2:
    return get_last_person_spread(a, k1)
  else:
    return get_last_person_spread(b, k2)

with open('C-large.in', 'r') as f:
  with open('c_large.out', 'w') as out:
    lines = [ x.strip() for x in f.readlines() ]
    T = int(lines[0])
    for i in xrange(T):
      data = lines[i+1].split(' ')
      N, k = int(data[0]), int(data[1])
      l, r = get_last_person_spread(N, k)
      out.write('Case #%d: %d %d\n' % (i+1, l, r))