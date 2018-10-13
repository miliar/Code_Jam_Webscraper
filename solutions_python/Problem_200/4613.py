# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer


def is_tidy(num):
    n1 = str(num)
    if len(n1) == 1:
        return True
    for r in range(0, len(n1) - 1):
        if int(n1[r]) > int(n1[r + 1]):
            break
        if r + 1 == len(n1) - 1:
            return True
    return False


for i in range(1, t + 1):
    n = int(input())
    for j in range(0, n):
        if is_tidy(n-j):
            print("Case #{}: {}".format(i, n-j))
            break


