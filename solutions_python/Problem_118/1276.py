def sqrt(n):
  left = long(n ** 0.49)
  right = long(n ** 0.51)
  while right - left > 1:
    current = long((right+left)/2)
    if current**2 > n:
      right = current
    else:
      left = current
  if n - left**2 < right**2 - n:
    return left
  else:
    return right

def check_palindrome(n):
  n_str = str(n)
  for i in range(len(n_str)/2):
    if n_str[i] != n_str[len(n_str)-i-1]:
      return False
  return True

def fair_and_square(min,max):
  total = 0
  for i in range(sqrt(min),sqrt(max)+1):
    if i*i < min:
      continue
    if i*i > max:
      break
    if check_palindrome(i) and check_palindrome(i*i):
      total += 1
  return total

for i in range(int(raw_input())):
  bounds = raw_input().split()
  print 'Case #%d: %d' % (i+1,fair_and_square(long(bounds[0]),long(bounds[1])))