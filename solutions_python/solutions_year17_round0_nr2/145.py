def tidy_num(target_num):
  temp_num = target_num
  digit_list = []
  while temp_num > 0:
    digit_list.append(temp_num % 10)
    temp_num /= 10
  
  num_length = len(digit_list)

  for i in xrange(1, num_length):
    if digit_list[num_length - i - 1] < digit_list[num_length - i]:
      next_try = target_num / (10 ** (num_length - i)) * 10 ** (num_length - i) - 1
      return tidy_num(next_try)

  return target_num

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  target_num = int(raw_input())
  print "Case #{}: {}".format(i, tidy_num(target_num))
  # check out .format's specification for more formatting options