def solve(N, K):
  chain = bin(K)[2:][-N:]
  return len(chain) == N and all(b == '1' for b in chain)

def main():
  f = open('snapper.in', 'r')
  lines = f.readlines()
  lines = [l.strip() for l in lines]
  f.close()

  T = int(lines[0])

  g = open('snapper.out', 'w')
  for i in xrange(1, T+1):
    N, K = [int(x) for x in lines[i].split()]
    result = 'ON' if solve(N, K) else 'OFF'
    g.write('Case #%s: %s\n' % (i, result))
  g.close()

if __name__ == '__main__':
  main()
  print 'Done.'
