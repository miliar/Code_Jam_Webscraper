# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    h = [n, ]
    current = n - 1
    for s in range(k):
        current = h.pop() - 1
        n1 = int(current / 2)
        h.append(n1)
        h.append(current - n1)
        h.sort()
        # print(h)
    print("Case #{}: {} {}".format(i, current - int(current / 2), int(current / 2)))
    # check out .format's specification for more formatting options
