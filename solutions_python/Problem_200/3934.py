t = int(raw_input())

for i in xrange(1, t + 1):
  n = int(raw_input())

  for x in xrange(n, 0, -1):  
    is_tidy = True
    
    prev_digit = 0
    for curr_digit in list(str(x)):
      if int(curr_digit) < prev_digit:
        is_tidy = False
        break
      prev_digit = int(curr_digit)
  
    if is_tidy:
      last_tidy_num = int(x)
      break

  print "Case #{}: {}".format(i, last_tidy_num)
