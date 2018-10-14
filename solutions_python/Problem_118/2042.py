import sys

def preprocess(d):
  if d == 'small':
    low = 1
    high = 31 # sqrt(1000)
  elif d == 'first-large':
    low = 1
    high = int(1e7) # sqrt(1e14)
  elif d == 'second-large':
    low = 1
    high = int(1e50) # sqrt(1e100)

  return [x for x in gen_squares(low, high) if is_palindrome(str(x))]

def gen_squares(low, high):
  for x in range(low, high + 1):
    if is_palindrome(str(x)):
      yield x ** 2

def is_palindrome(s):
  n = len(s)
  for i in range(n >> 1):
    if s[i] != s[n - i - 1]:
      return False
  return True

def solve(fns, low, high):
  count = 0
  for x in fns:
    if low <= x and x <= high:
      count += 1
  return count

def output(case, count):
  print('Case #{}: {}'.format(case, count))

if __name__ == '__main__':
  # d = 'small'
  d = 'first-large'
  # d = 'second-large'
  fns = preprocess(d)

  num_inputs = int(sys.stdin.readline())

  for i in range(num_inputs):
    [low, high] = sys.stdin.readline().split()
    low = int(low)
    high = int(high)
    count = solve(fns, low, high)
    output(i + 1, count)
