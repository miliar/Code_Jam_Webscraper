import sys

def shuffle(n,mylist):
  n_str = str(n)
  retval = [n]
  if len(n_str) == 1:
    return retval
  for i in range(1,len(n_str)):
    recycled = int(n_str[i:]+n_str[:i])
    if recycled in mylist and recycled not in retval:
      retval.append(recycled)
  return retval

ncases = int(sys.stdin.readline())
for case in range(1, ncases+1):
  current = sys.stdin.readline().split()
  A = int(current[0])
  B = int(current[1])
  output = 0
  numbers = range(A,B+1)
  while numbers != []:
    myset = shuffle(numbers[0],numbers)
    output = output + (len(myset) * (len(myset)-1) / 2)
    for i in myset:
      #assert(i in numbers)
      numbers.remove(i)
  print 'Case #' + str(case) + ': ' + str(output)
