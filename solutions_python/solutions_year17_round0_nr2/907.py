
def isAsendingOrder(n):
  str_n = str(n)
  l = len(str_n)
  v = [int(str_n[i]) for i in xrange(0, l)]
  for i in xrange(0, l-1):
    if(v[i] > v[i+1]):
      return False
  return True

def minimize(n):
  while(True):
    str_n = str(n)
    l = len(str_n)
    v = [int(str_n[i]) for i in xrange(0, l)]

    split_idx = -1
    for i in xrange(0, l-1):
      if(v[i] > v[i+1]):
        split_idx = i
        break

    if (split_idx == -1):
      break

    v[split_idx] -= 1
    for i in xrange(split_idx+1, l):
      v[i] = 9
    new_n = ''.join([str(i) for i in v])
    n = int(new_n)
  return n





 # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  datas = raw_input().split(" ")  # read a list of integers, 2 in this case
  n = int(datas[0])

  while(True):
    if(isAsendingOrder(n)):
      break
    n = minimize(n)

  print "Case #{}: {}".format(i, n)
  # check out .format's specification for more formatting options
