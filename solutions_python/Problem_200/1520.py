tests = int(input())
for t in range(tests):
  num = list(input())
  curr = 0
  length = len(num)

  for i in range(length):
    if num[i] > num[curr]:
      curr = i
    elif num[i] < num[curr]:
      num[curr] = str(int(num[curr]) - 1)
      for j in range(curr+1,length):
        num[j] = '9'
      break
  if num[0] == '0' and len(num) > 1:
    res = ''.join(num[1:])
  else:
    res = ''.join(num)
  print('Case #' + str(t+1) + ': ' + res)
