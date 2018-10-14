from sys import stdin





# N^2!!!! This is only going to work for the small test case .....
def solve(A, B, K):
  return sum([1 for a in range(A) for b in range(B) if (a&b < K)])


if __name__ == '__main__':
  T = int(stdin.readline())
  for case in xrange(T):
    inputs = map(int, stdin.readline().split())
    print 'Case #%d: %d' %(case+1, solve(*map(int,inputs)))
