import sys

if __name__ == '__main__':
   n_case = int(sys.stdin.readline())
   for ix_case in xrange(n_case):
      sys.stdin.readline()
      s_line = sys.stdin.readline().split()
      n_line = map(int, s_line)
      xor = reduce(lambda x, y: x^y, n_line)
      if xor is 0:
         ans = sum(n_line) - min(n_line)
      else:
         ans = 'NO'
      print('Case #%d: %s' % (ix_case+1, ans))
