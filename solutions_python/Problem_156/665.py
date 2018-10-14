import sys
from math import ceil

def main():
  infd = open(sys.argv[1])
  outfd = open(sys.argv[1] + '.out', 'w')
  T = int(infd.readline())
  for case in range(1, T+1):
    d = int(infd.readline())
    ps = map(int, infd.readline().split())
    outfd.write('Case #' + str(case) + ': ')
    outfd.write(str(solve(d, ps)) + '\n')
  infd.close()
  outfd.close()

# d = num diners with non empty plates
# ps = number of pancakes on each non-empty plate
def solve(d, ps):
  ps = list(reversed(sorted(ps)))
  factors = [{} for i in range(len(ps))]
  p_max = ps[0]
  for stack_height in range(1, p_max + 1):
    for i in range(len(ps)):
      p = ps[i]
      f = factors[i]
      # how many piles would it take for p to be divided into stacks of height <= stack_height
      f[stack_height] = int(ceil(float(p) / stack_height))
  # find optimum stack height
  min_mins = None
  for stack_height in range(1, p_max + 1):
    specials = 0
    for i in range(len(ps)):
      p = ps[i]
      f = factors[i]
      # -1 since we don't have to move the last pile of height <= stack_height
      specials += f[stack_height] - 1
    total_mins = specials + stack_height
    if min_mins is None or total_mins < min_mins:
      min_mins = total_mins
  return min_mins


main()
