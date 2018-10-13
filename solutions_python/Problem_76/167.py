#f = open('C-small-attempt0.in', 'r')
f = open('C-large.in', 'r')
#f = open('C-practice.in', 'r')
out = open('C.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
  N = int(f.readline().strip())
  C = [int(x) for x in f.readline().strip().split(' ')]
  
  if reduce(lambda x, y: x ^ y, C) > 0:
    out.write('Case #%d: NO' % (t + 1) + '\n')
    print 'Case #%d: NO' % (t + 1)
  else:
    out.write('Case #%d: ' % (t + 1) + str(sum(sorted(C)[1:])) + '\n')
    print 'Case #%d: ' % (t + 1) + str(sum(sorted(C)[1:]))

f.close()
out.close()
