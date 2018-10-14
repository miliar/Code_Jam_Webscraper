

def find_max_tidy(n, num_digits):
  n_below = (n / 10**(num_digits - 1)) * 10**(num_digits - 1)
  soft_max = n_below - 1
  
  if num_digits == 1:
    hard_max = n
  else:
    if (n - n_below) / 10 ** (num_digits - 2) < n /  10 ** (num_digits - 1):
      hard_max = -1
    elif (n - n_below) / 10 ** (num_diigts - 2) > n / 10 ** (num_digits - 1):
      hard_max = n_below + find_max_tidy(n - n_below, num_digits - 1)
  return max(soft_max, hard_max)
    
def solve2():
  cap = int(raw_input())
  num_digits = len(str(cap))
  return find_max_tidy(cap, num_digits)

def solve():
  digits = list(raw_input())
  digits = map(lambda x: int(x), digits)
  
  index = len(digits) - 1
  while index > 0:
    if digits[index - 1] > digits[index]:
      j = index
      digits[index-1] -= 1
      while j < len(digits):
        digits[j] = 9
        j += 1
    index -= 1
  retval = 0
  for i in digits:
    retval *= 10
    retval += i
  return retval


num_tests = int(raw_input())

for K in range(num_tests):
    print "Case #" + str(K + 1) + ": " + str(solve())
