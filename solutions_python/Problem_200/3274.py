def is_tidy(num):
    while num >= 10:
        if num % 10 < (num // 10) % 10:
            return False
        num = num // 10
    return True


# input() reads a string with a line of input, stripping the '\n' (newline) at
# the end.This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    num = int(input())
    count = 0
    while (not is_tidy(num)):
        num = num // 10 - 1
        count += 1
    print("Case #{}: {}".format(i, (str(num) + "9" * count).strip("0")))
    # check out .format's specification for more formatting options
