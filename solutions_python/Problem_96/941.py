import sys

ncases = int(sys.stdin.readline())
for case in range(1, ncases+1):
  current = sys.stdin.readline().split()
  ngooglers = int(current[0])
  nsurprises = int(current[1])
  p = int(current[2])
  totals = current[3:]
  output = 0
  
  for i in totals:
    t = int(i)
    if t%3 == 0:
      if t/3 >= p:
        output = output + 1
      elif t/3 > 0 and t/3+1 >= p and t/3+1 <= 10 and nsurprises > 0:
        output = output + 1
        nsurprises = nsurprises - 1
    elif t%3 == 1:
      if t/3+1 >= p:
        output = output + 1
    else:
      if t/3+1 >= p:
        output = output + 1
      elif t/3+2 >= p and t/3+2 <= 10 and nsurprises > 0:
        output = output + 1
        nsurprises = nsurprises - 1
  
  print 'Case #' + str(case) + ': ' + str(output)
