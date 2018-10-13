T = int(raw_input())

def make_tidy(n):
  lst = list(str(n))
  idx = len(lst)-1
  while idx > 0:
    if int(lst[idx-1]) > int(lst[idx]):
      lst[idx-1] = str(int(lst[idx-1])-1)
      for i in range(idx, len(lst)):
        lst[i] = '9'
      idx += 1
    idx -= 1
  return int(''.join(lst))

for i in range(T):
  print 'Case #' + str(i+1) + ': ' + str(make_tidy(int(raw_input())))