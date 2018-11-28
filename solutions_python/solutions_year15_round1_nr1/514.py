

INPUT_FILE = 'A-large.in'

def solve_case_1(intervals):
  total = 0
  for i in range(len(intervals) - 1):
    cur = intervals[i]
    nxt = intervals[i + 1]
    diff = max(0, cur - nxt)
    total += diff
  return total

def solve_case_2(intervals):

  def solve(rate):
    total = 0
    for i in range(len(intervals) - 1):
      cur = intervals[i]
      nxt = intervals[i+1]
      if cur - rate > nxt:
        return False
      else:
        total += min(rate, cur)
    return True, total

  def binary_search(low, high):
    assert low <= high
    if low == high:
      return high
    middle = int((low + high) / 2)
    if solve(middle):
      return binary_search(low, middle)
    else:
      return binary_search(middle + 1, high)

  res = binary_search(0, 10000000)
  return solve(res)[1]


with open(INPUT_FILE, 'r') as f:
  num_cases = int(f.readline())

  for case_num in range(num_cases):
    _ = f.readline()
    intervals = [int(x) for x in f.readline().split(' ')]
    print 'Case #{0}:'.format(case_num + 1), solve_case_1(intervals), solve_case_2(intervals)

