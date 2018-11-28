import sys

f = open(sys.argv[1])
lines = iter(f)
n = int(lines.next())
for i in xrange(1, n+1):
  first_answer = int(lines.next())
  first_rows = [set(int(x) for x in lines.next().split()) for j in xrange(4)]
  candidates1 = first_rows[first_answer - 1]

  second_answer = int(lines.next())
  second_rows = [set(int(x) for x in lines.next().split()) for j in xrange(4)]
  candidates2 = second_rows[second_answer - 1]

  candidate = candidates1 & candidates2
  if len(candidate) == 1:
    print 'Case #{}: {}'.format(i, list(candidate)[0])
  elif len(candidate) > 1: 
    print 'Case #{}: Bad magician!'.format(i)
  elif len(candidate) == 0: 
    print 'Case #{}: Volunteer cheated!'.format(i)
