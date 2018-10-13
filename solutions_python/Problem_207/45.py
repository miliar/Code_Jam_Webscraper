import sys

tests = input ()
for test in range (tests):
  n, r, o, y, g, b, v = map(int, sys.stdin.readline().split())

  res = ['-'] * n;
  assert (n == r + y + b)
  m = max (r, y, b)

  ns = [r, y, b]
  color = ['R', 'Y', 'B'];
  for i in range (2):
    for j in range (2):
       if ns[j] >ns[j+1]:
         ns[j], ns[j+1] = ns[j+1], ns[j]
         color[j], color[j+1] = color[j+1], color[j]

  if m > (n - m):
    res = "IMPOSSIBLE"
  else:
    for i in range (m):
       res[i * 2] = color[2]
    for i in range (n):
       if res[i] == '-':
         if res[(i-1)%n] != color[1] and ns[1] >= ns[0]:
           res[i] = color[1]
           ns[1] -= 1
         else:
           res[i] = color[0]
           ns[0] -= 1  
    res = "".join(res);
  print ("Case #" + str(test + 1) + ": " + res)
