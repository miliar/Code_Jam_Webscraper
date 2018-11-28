import sys

def helper(audience):
  num_additional = 0
  num_standing = 0
  for i in xrange(len(audience)):
    if audience[i] > 0 and num_standing < i:
      num_additional += (i - num_standing)
      num_standing = i
    num_standing += audience[i]
  return num_additional

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

num_tests, tests = parse_file(1)
for case,test in enumerate(tests):
  most_shy, audience_str = test[0].split()
  audience = [int(x) for x in list(audience_str)]
  sol = helper(audience)
  print 'Case #{}: {}'.format(case+1, sol)
  #sol = helper(test)
  #print 'Case #{}: {}'.format(case+1, sol)
