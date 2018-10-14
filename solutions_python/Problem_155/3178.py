import sys
f = iter(open(sys.argv[1]))
cases = int(f.next())
for case in xrange(cases):
  s_max, values = f.next().strip().split(' ')
  s_max = int(s_max)
  values = [int(c) for c in values]
  
  num_clapping = values[0]
  friends = 0
  for i, v in enumerate(values[1:], 1):
    new_friends = max(i - num_clapping, 0)
    friends += new_friends
    num_clapping += new_friends + v
  print 'Case #{}: {}'.format(case + 1, friends)
