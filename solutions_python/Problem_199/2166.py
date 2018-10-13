# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [list(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  # print("Case #{}: {} {}".format(i, n, m))

  m = int(''.join(m))
  count = 0
  flip = 0
  for x in n:
    if x == '+':
      count += 1
    else:
      if count + m > len(n):
        flip = 'IMPOSSIBLE'
        break
      flip += 1
      count += 1
      for j in range(count, count + m - 1):
        if (n[j] == '-'):
          n[j] = '+'
        else:
          n[j] = '-'

  print("Case #{}: {}".format(i, flip))