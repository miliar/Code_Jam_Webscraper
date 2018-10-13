def flip(line, k, start):
    flipped = ""
    for i in range(start, start + k):
        if line[i] == "-":
            flipped = flipped + "+"
        else:
            flipped = flipped + "-"
    return line[:start] + flipped + line[start + k:]


# input() reads a string with a line of input, stripping the '\n' (newline) at
# the end.This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
    line, k = input().split(" ")
    k = int(k)
    n = len(line)
    count = 0

    for i in range(n - k + 1):
        if line[i] == "-":
            line = flip(line, k, i)
            count = count + 1

    if line == "+" * n:
        print("Case #{}: {}".format(j, count))
    else:
        print("Case #{}: {}".format(j, "IMPOSSIBLE"))
    # check out .format's specification for more formatting options
