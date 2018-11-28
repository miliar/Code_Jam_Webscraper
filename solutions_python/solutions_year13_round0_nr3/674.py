#!/usr/bin/python
def palin(x):
  x = str(x)
  length = len(x)
  for i in range(length // 2):
    if x[i] != x[length-i-1]:
      return False
  return True

def sqrt(num, round_up):
  min=1
  max=num
  while min != max:
    middle = (min + max + 1) // 2
    middle_sqr = middle*middle
    if middle_sqr > num:
      max = middle - 1
    else:
      min = middle
      
  if min*min < num and round_up:
    return min+1
  else:
    return min

def pal_range_naive(min, max):  
  for X in range(min, max+1):
    palin(X)
  
  
def mirror(v, digits):
  v = str(v)
  if len(v) != (digits + 1) // 2:
    raise Exception()
  
  if digits % 2 == 0:
    return v + v[::-1]
  else:
    return v[:-1] + v[::-1]
  
def pal_range(value):
  value = str(value)
  digits = len(value)
  
  while True:
    valueDigits = (digits+1) // 2
    if value is None:
      value = 10L ** (valueDigits -1)
    else:
      value = long(value[:valueDigits])
    maxValue = 10L ** valueDigits
    while value < maxValue:
      yield long(mirror(value, digits))
      value = value + 1

    digits = digits+1
    value = None
    

n_tests = int(raw_input())
for test in range(1, n_tests+1):
  ret=0
  min, max = (long(x) for x in raw_input().split(' '))
  min, max = sqrt(min, True), sqrt(max, False)
  for X in pal_range(min):
    if X < min:
      continue
    if X > max:
      break
    if palin(X*X):
      ret = ret + 1

  print('Case #%i: %i' % (test, ret))