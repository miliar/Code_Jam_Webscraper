# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def pancake_num(pancake_string, K):
  string_length = len(pancake_string)
  pancake_list = []
  for i in xrange(string_length):
    num = 0
    if pancake_string[i] == '-':
      num = 1
    pancake_list.append(num)

  result = 0

  for i in xrange(string_length - K + 1):
    if pancake_list[i] == 1:
      result += 1
      for j in xrange(K):
        pancake_list[i+j] = (pancake_list[i+j] + 1) % 2

  is_success = True
  for i in pancake_list:
    if i == 1:
      is_success = False
      break

  if is_success:
    return result
  else:
    return "IMPOSSIBLE"


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  pancake_string, K = [s for s in raw_input().split(" ")]  
  K = int(K)
  print "Case #{}: {}".format(i, pancake_num(pancake_string, K))
  # check out .format's specification for more formatting options