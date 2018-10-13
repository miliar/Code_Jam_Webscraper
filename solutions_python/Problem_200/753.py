t = int(input())

for _ in range(t):
  s = input()
  s = list(s)
  n = len(s)
  for i in range(n):
    s[i] = int(s[i])
  i = 1
  while (i < n):
    if (s[i] >= s[i - 1]):
      i += 1
    else:
      s[i - 1] -= 1
      for j in range(i, n):
        s[j] = 9
      i = 1
  print('Case #', _ + 1 ,':', sep = '', end = ' ')
  for i in range(n):
    if (s[i] != 0):
      print(s[i], sep = '', end = '')
  print()
