def main():
  f = open('candy.in', 'r')
  g = open('candy.out', 'w')
  T = int(f.readline())
  for i in xrange(1, T+1):
    N = int(f.readline())
    strarr = f.readline().split(' ')
    V = [int(x) for x in strarr]
    V.sort()
    xor = 0
    for a in V:
      xor ^= a
    if xor != 0:
      g.write('Case #%s: NO\n' % i)
    else:
      sol = sum(V) - V[0]
      g.write('Case #%s: %s\n' % (i, sol))
  g.close()
  f.close()

if __name__ == '__main__':
  main()
