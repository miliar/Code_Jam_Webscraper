# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    stalls, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    distances = []
    distances.append(stalls)
    right = distances
    left = right
    while k >= 1:
        k -= 1
        maximum = max(distances)
        distances.remove(maximum)
        if maximum % 2 == 1:
            left = maximum//2
            right = left
        else:
            right = maximum//2
            left = right -1
        distances.append(left)
        distances.append(right)
    print("Case #{}: {} {}".format(i, max(left, right), min(left, right)))
# check out .format's specification for more formatting options
