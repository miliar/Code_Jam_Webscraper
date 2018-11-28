# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    d, n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    time=list()
    for j in range(n):
        k, s = [int(p) for p in input().split(" ")]    
        time.append((d-k)/s)
    out=d/max(time)
    print("Case #{}: {}".format(i, out))
  # check out .format's specification for more formatting options