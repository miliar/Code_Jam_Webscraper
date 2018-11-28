def tidy(inp):
    dig = [int(j) for j in str(inp)]

    if dig == sorted(dig):
        return True
    return False


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    x = int(input())
    while not tidy(x):
        x -= 1
    print("Case #{}: {}".format(i, x))

