x = int(input())
for num in range(1, x + 1):
  curr = input()
  d = int(curr.split(' ')[0])
  n = int(curr.split(' ')[1])
  s = -1;
  for j in range(1, n + 1):
    curr = input()
    k = int(curr.split(' ')[0])
    i = int(curr.split(' ')[1])
    t = (d - k)/i
    if t > s:
      s = t
  print('Case #' + str(num) + ': {0:.6f}'.format(d/s))
