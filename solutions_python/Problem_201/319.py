import sys

T = int(sys.stdin.readline().rstrip('\n'))

def solve (N, K):
  i = 0
    
  while (2 << i) < K + 1: i += 1

  least = (N + 1 - (1 << i)) // (1 << i)
  remainder = K + 1 - (1 << i)

  if least * (1 << i) + remainder <= (N + 1 - (1 << i)):
      return least + 1
  else:
      return least

for Q in range(1, T + 1):
  line = sys.stdin.readline().rstrip('\n').split(' ')
  N = int(line[0])
  K = int(line[1])

  gap = solve(N, K)

  if gap % 2 == 1:
    print 'Case #{}: {} {}'.format(Q, gap / 2, gap / 2)
  else:
    print 'Case #{}: {} {}'.format(Q, gap / 2, gap / 2 - 1)
  
