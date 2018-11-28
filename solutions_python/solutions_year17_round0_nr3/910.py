import collections
import math
import sys

fin = sys.stdin

def main():
  num_cases = int(fin.readline().strip())
  for i in range(num_cases):
    case_num = i + 1
    n, k = [int(k) for k in fin.readline().strip().split()]

    value = solve(n, k)
    output = '%d %d' % tuple(split(value))
    print('Case #%d: %s' % (case_num, output))

def solve(n, k):
  current = {n: 1}
  current_size = total(current)
  while k > current_size:
    k -= current_size
    current = iterate(current)
    current_size = total(current)

  # print current
  # print current_size
  # print k
  for key, value in reversed(sorted(current.iteritems())):
    if k > value:
      k -= value
    else:
      return key

def iterate(spec):
  rv = collections.defaultdict(int)
  for k, v in spec.iteritems():
    for child in split(k):
      rv[child] += v
  return rv

def split(k):
  half = (k - 1) / 2.0
  return [int(math.ceil(half)), int(math.floor(half))]

def total(spec):
  return sum(spec.values())

if __name__ == '__main__':
  main()
