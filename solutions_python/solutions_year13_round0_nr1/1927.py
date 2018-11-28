import io

def check(M, S):
  diag = all([M[i][i] in S for i in xrange(4)])
  diag |= all([M[3-i][i] in S for i in xrange(4)])
  if diag: return True

  for row in xrange(4):
    if all([M[row][col] in S for col in xrange(4)]):
      return True

  for col in xrange(4):
    if all([M[row][col] in S for row in xrange(4)]):
      return True

  return False

def main():
  N = int(raw_input())
  for testcase in xrange(1, N+1):
    M = [raw_input() for i in xrange(4)]
    raw_input() # discard empty line

    if check(M, 'XT'):
      print 'Case #{0}: {1}'.format(testcase, 'X won')
      continue

    if check(M, 'OT'):
      print 'Case #{0}: {1}'.format(testcase, 'O won')
      continue

    if all([row.find('.') == -1 for row in M]):
      print 'Case #{0}: {1}'.format(testcase, 'Draw')
      continue

    print 'Case #{0}: {1}'.format(testcase, 'Game has not completed')

if __name__ == '__main__':
  main()
