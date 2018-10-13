import sys
N = int(sys.stdin.readline())

for t in range(1, N + 1):
  r0 = int(sys.stdin.readline())
  b0 = [[int(j) for j in sys.stdin.readline().split(' ')] for i in range(4)]
  r1 = int(sys.stdin.readline())
  b1 = [[int(j) for j in sys.stdin.readline().split(' ')] for i in range(4)]
  inter = set(b0[r0 - 1]).intersection(set(b1[r1 - 1]))
  sys.stdout.write('Case #%d: ' % t)
  if len(inter) == 1:
    sys.stdout.write('%d\n' % inter.pop())
  elif len(inter) != 0:
    sys.stdout.write('Bad magician!\n')
  else:
    sys.stdout.write('Volunteer cheated!\n')
