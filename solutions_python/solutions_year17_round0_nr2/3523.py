def tidy(n):
  level = 10
  largest = 0
  dec = 0
  next = 0
  replacement = 0

  for i in range(len(str(n)) - 1):
    next = ((n%level)/(level/10)) - dec
    nextNext = ((n%(level*10))/(level))

    if next == 0 or (nextNext > next) :
      next = 9
      dec = 1
      largest = (next * (level/10)) + replacement
    else:
      dec = 0
      largest = largest + (next * (level/10))

    level = level * 10
    replacement = (replacement * 10) + 9

  next = ((n%level)/(level/10)) - dec
  return largest + (next * (level/10))


#main program
test_cases = int(raw_input())

for i in range(test_cases):
  test = int(raw_input())
  t_result = tidy(test)

  print "Case #{0}: {1}".format(i + 1, t_result)