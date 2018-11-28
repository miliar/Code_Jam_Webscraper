def flip_pancake(pancakes, k, ps):
  idx = -1
  for i in xrange(0, ps-k+1):
    if pancakes[i] == '-':
      idx = i
      break
  if idx == -1:
    return pancakes

  for j in xrange(idx, idx+k):
    if pancakes[j] == '-':
      pancakes[j] = '+'
    else:
      pancakes[j] = '-'
  return pancakes


 # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  datas = raw_input().split(" ")  # read a list of integers, 2 in this case
  pancakes = list(datas[0])
  k = int(datas[1])

  flip = 0
  ps = len(datas[0])
  prev_pancakes = ['+'] * ps
  while (True):
    if all( '+' == c for c in pancakes ):
      break

    if prev_pancakes == pancakes:
      flip = -1
      break

    prev_pancakes = pancakes[:]

    pancakes = flip_pancake(pancakes, k, ps)
    flip += 1

  if flip == -1:
    result_str = 'IMPOSSIBLE'
  else:
    result_str = str(flip)
  print "Case #{}: {}".format(i, result_str)
  # check out .format's specification for more formatting options
