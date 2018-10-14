class AIB(object):

  def __init__(self, maxValue):
    self.maxValue = maxValue
    self.tree = [0] * (maxValue + 1)

  def update(self, idx, value=1):
    while idx <= self.maxValue:
      self.tree[idx] += value
      idx += (idx & -idx)

  def read(self, idx):
    result = 0
    while idx > 0:
      result += self.tree[idx]
      idx -= (idx & -idx)
    return result

def solve(V):
  V.sort(key=lambda i: i[0])
  tree = AIB(max(i[1] for i in V))
  result = 0
  for i in xrange(len(V)):
    A, B = V[i]
    result += i - tree.read(B)
    tree.update(B)
  return result

def main():
  f = open('rope.in', 'r')
  g = open('rope.out', 'w')

  T = int(f.readline().strip())

  for i in xrange(1, T+1):
    # Read testcase.
    N = int(f.readline().strip())
    V = [None] * N
    for j in xrange(N):
      strarr = f.readline().strip().split()
      A = int(strarr[0])
      B = int(strarr[1])
      V[j] = (A, B)

    # Solve testcase.
    result = solve(V)

    # Print testcase.
    g.write('Case #%s: %s\n' % (i, result))
    # print 'Case #%s: %s' % (i, result)

  f.close()
  g.close()

if __name__ == '__main__':
  main()
  print 'Done.'
