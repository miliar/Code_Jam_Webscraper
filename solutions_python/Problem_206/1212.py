# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    d, n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    maxT = 0;
    for j in range(n):
        k, s = [int(s) for s in input().split(" ")]
        t = (d-k)/s
        maxT = max(maxT, t)
    print("Case #{}: {}".format(i, d/maxT))
