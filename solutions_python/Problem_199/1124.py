# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for c in range(1, t + 1):
  n, m = input().split(" ")  # read a list of integers, 2 in this case
  k = int(m)
  possible = True
  steps = 0
  
  s = list(n)
  for i in range(len(s)-k+1):
    if s[i] == '-':
      steps += 1
      for j in range(k):
        s[i+j] = '-' if s[i+j] == '+' else '+'  
  possible = s[len(s)-k:] == ['+',]*k
  print("Case #{}: {}".format(c, steps if possible else "IMPOSSIBLE"))
