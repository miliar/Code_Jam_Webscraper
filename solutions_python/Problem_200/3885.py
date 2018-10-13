test_cases = int(raw_input())

for i in xrange(1, test_cases + 1):
  case = raw_input()
  while case != ''.join(sorted(case)):
    case = str(int(''.join(case)) - 1)
  print "Case #{}: {}".format(i, int(''.join(case)))
