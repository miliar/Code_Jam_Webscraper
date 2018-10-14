# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for c in range(1, t + 1):
  d, n = map(int, input().split(" "))  # read a list of integers, 2 in this case
  horses = []
  for h in range(n):
    horses.append(tuple(map(int, input().split())))

  horses.sort(key=lambda x: x[0])

  max_time = 0
  for h in horses:
    time = (d-h[0]) / h[1]
    max_time = max(time, max_time)
 
  print("Case #{}: {:.6f}".format(c, d/max_time))
