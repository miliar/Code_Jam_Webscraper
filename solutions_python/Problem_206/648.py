# Input
#
# 3
# 2525 1
# 2400 5
# 300 2
# 120 60
# 60 90
# 100 2
# 80 100
# 70 10
#
# Output
#
#
# Case #1: 101.000000
# Case #2: 100.000000
# Case #3: 33.333333
#



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  D, N = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  max = 0
  for j in range(N):
    S, U = [int(s) for s in input().split(" ")]
    T = (D-S)/U
    if T > max:
      max = T
  speed = D/max
  print("Case #{}: {}".format(i, speed))