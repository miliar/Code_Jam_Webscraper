# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = [int(s) for s in input()]  # read a list of integers, 2 in this case
    # print("Case #{}: {}".format(i, n))

    c = len(n) - 1
    for x in reversed(n):
        if c <= 0:
            break
        if n[c-1] > n[c]:
            n[c-1] -= 1
            n[c:] = [9]*(len(n) - c)
        c -= 1
    end = int(''.join(str(e) for e in n))
    print("Case #{}: {}".format(i, end))
