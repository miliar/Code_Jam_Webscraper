def flip(n, k):
  n = [c == '+' for c in n]
  f = 0
  for i in xrange(len(n) - k + 1):
    if not n[i]:
      f += 1
      for j in xrange(k):
        n[i + j] = not n[i + j]
  if all(n):
    return str(f)
  return 'IMPOSSIBLE'

def solve(name):
  f = open(name, 'r')
  c = int(f.readline())
  for i in xrange(c):
    l = f.readline().split(' ')
    print 'Case #%d: %s' % (i + 1, flip(l[0], int(l[1])))
  f.close()

def main():
  solve('A-large.in.txt')

if __name__ == '__main__':
  main()

