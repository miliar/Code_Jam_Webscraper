
filename = 'large'

cases = open(filename + '.in').readlines()
cases = [map(int,case.split(' ')[1].strip()) for case in cases[1:]]

out = open(filename + '.out','w')

for nr, case in enumerate(cases):
  standing = 0
  invites = 0
  for i, k in enumerate(case):
    invites += max(0, i - (standing+invites))
    standing += k
  print('Case #{}: {}'.format(nr+1,invites), file=out)
