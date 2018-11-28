import sys

rl = lambda : sys.stdin.readline().strip()

def solve_case(case_num, C, F, X):
  def next_sum():
    i = 0
    sum = 0
    gen = 2 + i * F
    while True:
      sum += C / gen
      i += 1
      gen = 2 + i * F
      yield sum, gen

  min = X / 2
  for time_farm, gen in next_sum():
    cur = time_farm + X / gen
    if cur >= min:
      break
    min = cur

  print "Case #%d: %.7f" % (case_num, min)

def main():
  num_cases = int(rl())
  for i in xrange(num_cases):
    C, F, X = [float(f) for f in rl().split()]
    solve_case(i+1, C, F, X)

main()

