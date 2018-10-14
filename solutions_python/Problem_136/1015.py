def solve(C, F, X):
  cur_min, n = X / 2., 1
  partial_sum = 0

  while True:
    partial_sum += C / (2. + (n - 1) * F)
    tmp = partial_sum + X / (2. + n * F)
    n += 1

    if tmp > cur_min:
      break
    else:
      cur_min = tmp
  return cur_min

if __name__ == '__main__':
  T = input()

  for case in xrange(1, T+1):
    C, F, X = [float(x) for x in raw_input().split()]

    print 'Case #%d: %.7f' % (case, solve(C, F, X))