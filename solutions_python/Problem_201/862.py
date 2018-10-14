# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  d = 1 << k.bit_length()-1
  n1 = (n-k+d) // d
  print("Case #{}: {} {}".format(i, n1//2 ,(n1-1)//2))
  # check out .format's specification for more formatting options
