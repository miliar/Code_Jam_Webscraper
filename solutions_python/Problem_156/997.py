import sys
import math

seen = {}

def helper(pancakes_left):
  global seen
  nonzero_pancakes_left = [x for x in pancakes_left if x > 0]
  if len(nonzero_pancakes_left) == 0:
      return 0
  nonzero_pancakes_left = sorted(nonzero_pancakes_left)

  largest = nonzero_pancakes_left[len(nonzero_pancakes_left)-1]
  start_largest = len(nonzero_pancakes_left)-1

  for i in xrange(len(nonzero_pancakes_left)-1, -1, -1):
    if nonzero_pancakes_left[i] == largest:
      start_largest = i
    else:
      break

  num_largest = len(nonzero_pancakes_left) - start_largest 

  if largest == 1:
    return 1
  if largest == 2:
    return 2
  if largest == 3:
    return 3

  factors = range(2, int(math.floor(math.sqrt(largest))) + 2)
  factor_scores = [largest] * len(factors)

  #print largest, factors
  for (i, f) in enumerate(factors):
    #if (len(pancakes_left) == 1):
    #    print pancakes_left, i, f
    if (f-1)*num_largest >= largest:
        continue
    parts = [largest / f] * f
    remainder = largest % f
    if remainder > 0:
      for j in xrange(remainder):
        parts[j] += 1
    if sum(parts) != largest:
      print "ERROR: sum of parts (" + str(sum(parts)) + ") should be equal to largest (" + str(largest) + ")"
    new_pancakes_left = nonzero_pancakes_left[:start_largest]
    new_pancakes_left += parts * num_largest
    seen_key = " ".join([str(x) for x in sorted(new_pancakes_left)])
    if seen_key not in seen:
        seen[seen_key] = helper(new_pancakes_left)

    factor_scores[i] = (f-1)*num_largest + seen[seen_key]

  nomove = 1 + helper([x-1 for x in nonzero_pancakes_left])
  return min([nomove] + factor_scores)

def parse_file(num_lines):
  with open(sys.argv[1], 'r') as f:
    lines = [l.rstrip('\n') for l in f.readlines()]
  i = 1
  tests = []
  while i < len(lines):
    new_test = []
    for j in range(num_lines):
      new_test.append(lines[i])
      i += 1
    tests.append(new_test)
  return int(lines[0]), tests

num_tests, tests = parse_file(2)
for case,test in enumerate(tests):
  D = int(test[0])
  pancakes_left = [int(x) for x in test[1].split()]
  sol = helper(pancakes_left)
  print 'Case #{}: {}'.format(case+1, sol)
  #sol = helper(test)
  #print 'Case #{}: {}'.format(case+1, sol)
