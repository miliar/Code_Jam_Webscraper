def tidy(n):
  s = str(n)
  for i in range (len (s) - 1):
    if s[i] > s[i+1]:
      return False
  return True

tests = input ()
for test in range (tests):
  n = input ()
  res = n
  p = 10
  while (not tidy(res)):
    res = res - res % p - 1
    p *= 10 
  print ("Case #" + str(test + 1) + ": " + str(res))
