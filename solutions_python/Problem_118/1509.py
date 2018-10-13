def palindrome_gen(a, b):
  a, b = int(a), int(b)
  s_a, s_b = str(a), str(b)
  l_a, l_b = len(s_a), len(s_b)
  for d in range(l_a, l_b+1):
    odd = d % 2
    h = d // 2
    if h == 0:
      for i in range(10):
        if a <= i <= b:
          yield i
      continue
    for i in range(10**h):
      y = str(i).zfill(h)
      if odd:
        for i in range(10):
          t = y[::-1] + str(i) + y
          x = int(t)
          if a <= x <= b and str(x) == t:
            yield x
      else:
        t = y[::-1] + y
        x = int(t)
        if a <= x <= b and str(x) == t:
          yield x


def ispalindrome(x):
  s = str(x)
  l = len(s)
  h = l // 2
  if s[:h] == s[::-1][:h]:
    return True
  return False

import math

# def issquare(x):
#   y = math.sqrt(x)
#   if y == int(y):
#     return True

def fairandsquare(a, b):
  result = set()
  # k = math.sqrt(b)
  k, t = (int(math.sqrt(x)) for x in (a,b))
  # for x in palindrome_gen(a, b):
  for x in palindrome_gen(k, t):
    square = x**2
    if square < a:
      continue
    if ispalindrome(square):
      result.add(x)
  return result

if __name__ == '__main__':
  import sys
  args = sys.argv[1:]
  if not args:
    exit(0)
  file = open(args[0], 'r')
  # for line in file.readlines():
  case_count = int(file.readline().strip())
  for n in range(1, case_count+1):
    a, b = (int(x) for x in file.readline().strip().split())
    # print(a, b)
    # print(fairandsquare(a, b))
    print('Case #{}: {}'.format(n, len(fairandsquare(a, b))))

